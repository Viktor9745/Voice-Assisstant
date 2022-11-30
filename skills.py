import os, webbrowser, sys, requests, subprocess, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speaker(text):
    engine.say(text)
    engine.runAndWait()

def browser():
    webbrowser.open('https://www.google.com', new=2)

def offpc():
    os.system('shutdown')

def weather():
    print('weather')

def telegram():
    subprocess.Popen('C:/Users/Yerkebulan/AppData/Roaming/Telegram Desktop/Telegram.exe')

# def game():
#     subprocess.Popen()

def offbot():
    sys.exit()
