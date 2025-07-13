import os
from voice import speak

def open_app(command):
    if "chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "notepad" in command:
        os.system("notepad")
    elif "calculator" in command:
        os.system("calc")
    else:
        speak("App not found.")