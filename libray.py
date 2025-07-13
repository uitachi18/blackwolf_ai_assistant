import subprocess
import sys

required_packages = [
    "pyttsx3",
    "SpeechRecognition",
    "schedule",
    "pyaudio",
    "tkinter",
    "webbrowser",
    "threading"
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("🔧 Installing required packages for GauravBot v1.0...")
for pkg in required_packages:
    try:
        install(pkg)
        print(f"✅ Installed: {pkg}")
    except Exception as e:
        print(f"❌ Failed to install {pkg}: {e}")

print("🎉 All done! You can now run GauravBot v1.0 with: python main.py")