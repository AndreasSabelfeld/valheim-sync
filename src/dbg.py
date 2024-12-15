import sys, traceback as tb
from dotenv import load_dotenv, dotenv_values

oldhook = sys.excepthook

def waitexcepthook(type, exception, traceback):
    oldhook(type, exception, traceback)
    input()

sys.excepthook = waitexcepthook

