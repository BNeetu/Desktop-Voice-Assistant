

import pyautogui as pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from time import sleep
import pyautogui
from datetime import date
import psutil
import cv2
import smtplib
from requests import get
import pywhatkit as kit
import pywhatkit
import sys




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring mam. Have a nice day!")

    elif hour>=12 and hour<18:
        speak("Good afternoon mam!")

    else:
        speak("Good evening mam!")

    speak("I am Jarvis mam. Please tell me how i may help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n",)

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhatineetu27@gmail.com', 'Rawat@7777')
    server.sendmail('bhatineetu27@gmail.com', to, content)
    server.close()


class Kit:
    pass


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
    # logic  for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia... please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("mam, what should i search on youtube")
            bm = takeCommand().lower()
            webbrowser.open(f"{bm}")

        elif 'open google' in query:
            speak("mam, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'play some music for me' in query or 'play music' in query or 'play some music' in query or 'could you play some song' in query:
            speak('playing music for you mam...')
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'play' in query or 'can you play' in query or 'please play' in query:
            speak("ok! here you go!!")
            query = query.replace("play", "")
            query = query.replace("could you play", "")
            query = query.replace("please play", "")
            webbrowser.open(f'https://open.spotify.com/search/{query}')
            sleep(15)
            pyautogui.click(x=1055, y=617)
            print("Enjoy your song!")
            speak("Enjoy your song mam!")

        elif 'what is the time' in query or 'please tell me the time' in query or 'time please' in query :
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("its", current_time)
            speak("the time is")
            speak(current_time)

        elif 'date please' in query or 'today"s date' in query or 'what is the date today' in query :
            today = date.today()
            current_date = today.strftime("%B %d %Y")
            print("today's date is ", current_date)
            speak("today's date is")
            speak(current_date)

        elif 'how much power we left' in query or'battery' in query or 'battery status' in query :
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"mam our system have {percentage} percent battery")

        elif 'open command prompt' in query:
            os.system("start cmd")
            speak("here you go mam!")


        elif 'open vs code' in query:
            codePath = "C:\\Users\\Neetu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("here you go mam")

        elif 'thank you' in query:
            speak("welcome mam...")


        elif 'how are you' in query:
            speak("i am good mam. thank you for asking")

        elif 'send email to neetu' in query or 'send email to' in query or 'please send email to ' in query:
            try:
                speak("what should i say ?")
                content = takeCommand().lower()
                to = "ns9583234@gmail.com"
                speak("Subject to your email!")
                sendEmail(to, content)
                speak("email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry mam . there being an error to send this email")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
            print("your ip address", ip)

        elif 'send the message' in query or 'send message' in query or 'message' in query:
            pywhatkit.sendwhatmsg("+918006640116", "this is testing protocol", 18,17)

        elif 'play song on youtube' in query:
            kit.playonyt("see you again")

        elif 'no thanks' in query:
            speak("thanks for using me mam", "have a good day.")
            sys.exit()

        speak("do you have any other work")