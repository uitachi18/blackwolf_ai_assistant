import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import webbrowser

from voice import speak, listen
from apps import open_app
from alarm import set_alarm
import schedule

root = tk.Tk()
root.title("blackwolf v1.0")

entry = tk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)

output = scrolledtext.ScrolledText(root, width=70, height=20)
output.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

def display_response(text):
    output.insert(tk.END, text + "\n")
    output.see(tk.END)

def run_text_command():
    command = entry.get()
    entry.delete(0, tk.END)
    display_response(f"You typed: {command}")
    handle_command(command.lower())

def run_voice_command():
    command = listen()
    display_response(f"You said: {command}")
    handle_command(command.lower())

def handle_command(command):
    if "open" in command:
        open_app(command)
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
        display_response(f"Searching for: {query}")
    elif "set alarm" in command:
        try:
            words = command.split()
            hour = int(words[-2])
            minute = int(words[-1])
            result = set_alarm(hour, minute)
            display_response(result)
        except:
            speak("Please say the time like 'set alarm for 7 30'")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        root.quit()
    else:
        speak("Command not recognized.")
        display_response("Command not recognized.")

tk.Button(root, text="Run Command", command=run_text_command).grid(row=0, column=1, padx=5)
tk.Button(root, text="🎤 Voice Command", command=run_voice_command).grid(row=0, column=2, padx=5)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule, daemon=True).start()

speak("blackwolf v1.0 is ready.")
display_response("Welcome to blackwolf v1.0!")

root.mainloop()