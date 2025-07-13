import schedule
from voice import speak

def set_alarm(hour, minute):
    time_str = f"{hour:02d}:{minute:02d}"
    schedule.every().day.at(time_str).do(lambda: speak("⏰ Alarm ringing!"))
    speak(f"Alarm set for {time_str}")
    return f"Alarm set for {time_str}"