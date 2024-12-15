import os

from dotenv import load_dotenv, dotenv_values
from tkinter import messagebox
from win10toast import ToastNotifier
from time import sleep

from src.dbox_handler import DBoxHandler
from src.valheim_detector import ValheimDetector
import src.dbg

def main():
    print("running...")
    # loading variables from .env file
    load_dotenv()
    WORLD_NAME = os.getenv("WORLD_NAME")

    toaster = ToastNotifier()

    toaster.show_toast("running... ", "Valheim-Sync has been started.", icon_path="valheim_sync.ico")
    dropbox = DBoxHandler(os.getenv("APP_KEY"), os.getenv("APP_SECRET"), os.getenv("REFRESH_TOKEN"), toaster)
    valheim = ValheimDetector(WORLD_NAME, dropbox, toaster)
    running = True
    sleep_duration = 1

    while running:
        if valheim.game_started():
            dropbox.download_save_files(valheim.path, WORLD_NAME)
            valheim.initial_read()

        if valheim.files_changed():
            dropbox.upload_save_files(valheim.path, WORLD_NAME)

        sleep(sleep_duration)

if __name__ == "__main__":
    main()
