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

def game():
    subprocess.Popen('C:/Program Files/Counter-Strike Source/Run_CSS.exe')

def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	try:
		params = {'q': 'Almaty', 'units': 'metric', 'lang': 'ru', 'appid': '4db0bcb363208ddf403a9da11323059e'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
	except:
		speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

def telegram():
    subprocess.Popen('C:/Users/Yerkebulan/AppData/Roaming/Telegram Desktop/Telegram.exe')

# def game():
#     subprocess.Popen()

def offbot():
    sys.exit()
