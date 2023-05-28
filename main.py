from time import strftime
import pickle
from tkinter import Label
import tkinter.messagebox
import tkinter as tk
import time as t
import subprocess as sub
from playsound import playsound as play
import os
import ast
import numpy as np
import random
import pandas as pd
from sklearn.linear_model import LinearRegression
import webbrowser as web
import pyautogui as pg
import wikipedia as wiki
import pywhatkit as kit
import pyjokes as jokes
import requests as rq
from math import degrees
from bs4 import BeautifulSoup
import pyttsx3
import datetime
from time import *
import speech_recognition as speech


toss = ["head", "tails"]

byes = {"au revoir its bye in French",
        "do svidaniya its bye in Russian",
        "adiós its bye in Spanish",
        "Zàijiàn its bye in Chineese"
        "Zàijiàn its bye in Chineese",
        "addio its bye in Italian",
        "Sayōnara its bye in Japeneese",
        "Tschüss its bye in German",
        "alavida its bye in hindi"}
# greets
greets = ["Hola! that's hello in Spanish!",
          "Salut! that is hi in French",
          "Anneyonghaseyo! that is hello in Korean",
          "Hallo! that is hi in German!",
          "Ciao! That's hi in Intalian!"]


# print(...)

E = pyttsx3.init("sapi5")

M = ["What can you see in darkness",
    "what starts with 1 and ends with none",
    "which was the tallest mountain before mount Everest was discovered",
    "which is the largest city in the world",
    "what is green but when fallen turns yellow ?",
    "I am a part of your home niether inside nor outside. Who am I ",
    "which month has 28 days ? ",
    "what ends with end? "]

voices = E.getProperty('voices')
E.setProperty('voice', voices[1].id)
hour = int(t.strftime('%H'))

def wish():
    if (hour >= 24):
        speak("Good Afternoon! ")
        print("Good Afternoon! ")
        E.runAndWait()
    if (hour < 12):
        speak("Good Morining! ")
        print("Good Morning! ")
        E.runAndWait()
    if (hour >= 18):
        speak("Good Evening! ")
        print("Good Evening! ")
        E.runAndWait()


class Exception():
    pass
    print('')

def speak(audio):
    E.say(audio)
    E.runAndWait()


wish()
print("I am your Jarvis! ")
print("What can I do for you")
speak("I am Jarvis! ")
speak("What can I do for you")

while True:
    try:
        r = speech.Recognizer()
        with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening . . . . .")
            audio = r.listen(source)

        userA = r.recognize(audio).lower()
        userA = userA.lower()
        speak("OK")

        if 'chrome' in userA:
            print("opening. .....")
            speak("opening chrome. .....")
            E.runAndWait()
            open = sub.Popen(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'add' in userA:
            speak("Surely I can do that.")
            E.runAndWait()
            speak("Please type the first number")
            E.runAndWait()
            num1 = int(input("Please type the first number:- "))
            speak("Please enter the second number.")
            E.runAndWait()
            num2 = int(input("Please type the second number:- "))
            num3 = num1+num2
            speak(num3)
            E.runAndWait()

        elif 'subtract' in userA:
            speak("Sure sir.")
            E.runAndWait()
            speak("Please type the first number")
            E.runAndWait()
            numo = int(input("Please type the first number:- "))
            speak("Please enter the second number")
            E.runAndWait()
            nump = int(input("Please type the second number:- "))
            numu = numo-nump
            speak(numu)
            E.runAndWait()

        elif 'multiplication' in userA:
            speak("Sure sir I will do that for you!.")
            E.runAndWait()
            speak("Please type the first number")
            E.runAndWait()
            numr = int(input("Please type the first number:- "))
            speak("Please enter the second number:- ")
            E.runAndWait()
            numk = int(input("Please type the second number:- "))
            speak(f"the multiplication is {numk*numr}")
            E.runAndWait()

        elif 'division' in userA:
            speak("At work. Right now!")
            E.runAndWait()
            speak("Please type the first number")
            E.runAndWait()
            numb = int(input("Please type the first number:- "))
            speak("Please enter the second number:- ")
            E.runAndWait()
            nums = int(input("Please type the second number:- "))
            numm = numb/nums
            speak(numm)
            E.runAndWait()

        elif 'area of a triangle' in userA:
            speak("Doing it sir!")
            E.runAndWait()
            speak("Please type the base:- ")
            E.runAndWait()
            ans1 = int(input("Please type the base:- "))
            speak("Please enter the hieght:- ")
            E.runAndWait()
            ans2 = int(input("Please type the hieght:- "))
            ans3 = (ans1 * ans2) / 2
            speak(f"The area of a triangle is {ans3}")
            print(f"The area of a triangle is {ans3}")
            E.runAndWait()

        elif 'perimeter of a square' in userA:
            speak("Doing it for sir!")
            E.runAndWait()
            speak("Please type the first side")
            E.runAndWait()
            num1 = int(input("Please type the first side:- "))
            num3 = num1*4
            speak("Here it is:-")
            speak(num3)
            E.runAndWait()

        elif 'play' in userA:
            video = userA.replace('play', '')
            speak(f'playing {video}')
            print("playing . .....")
            E.runAndWait()
            kit.playonyt(video)

        elif 'temperature' in userA:
            speak('Enter the Place')
            place = input('Enter the Place:- ').lower()
            search = f'temeperature of {place}'
            url = f"https://www.google.com/search?q={search}"
            r = rq.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            temp = data.find("div", class_="BNeawe").text
            speak(f"The current {search} is {temp}")
            print(f"The current {search} is {temp}")

        elif 'iphone' in userA:

            speak('Enter The Model Number of Iphone')
            i_model = float(input('Enter The Model Number of Iphone:- '))            
            data = pd.read_csv("D:\\Rigved\\Python2\\Machine Learning\\Iphone Price Prediction\\Iphone_price.csv")

            model = LinearRegression()
            model.fit(data[['version']], data[['price']])

            pred = int(model.predict([[i_model]]))
            print(f'Price of Iphone {i_model} would be Rupees {pred}')
            speak(f'Price of Iphone {i_model} would be Rupees {pred}')

        elif 'time' in userA:
            now = datetime.datetime.now()
            speak("The currnt time is: ")
            E.runAndWait()
            speak(now.strftime("%I:%M:%S"))
            print(now.strftime("%I:%M:%S"))
            E.runAndWait()

        elif 'date' in userA:
            now = datetime.datetime.now()
            speak("The current date is:")
            E.runAndWait()
            speak(now.strftime("%D:%M:%Y"))
            print(now.strftime("%D:%M:%Y"))
        elif 'clock' in userA:

            # importing strftime function to
            # retrieve system's time
            speak("opening Clock. .")
            E.runAndWait()

            # creating tkinter window
            root = tk.Tk()
            root.title('Clock')

            def time():
                string = strftime('%I:%M:%S %p')
                now.config(text=string)
                now.after(200, time)

            # Styling the label widget so that clock
            # will look more attractive
            now = Label(root, font=('Times in Roman', 40, 'bold'),
                        background='black',
                        foreground='white')

            # Placing clock at the centre
            # of the tkinter window
            now.pack(anchor='center')
            time()

            root.mainloop()

        elif 'notepad' in userA:
            speak("opening notepad. ")
            sub.Popen("C:\\WINDOWS\system32\\notepad.exe")
            E.runAndWait()

        elif "joke" in userA:
            speak("Here it is!")
            E.runAndWait()
            print(jokes.get_joke())
            E.runAndWait()
            speak("ha ha ha ha ha")
            E.runAndWait()

        elif "gpt" in userA:
            speak("opening gpt. ")
            E.runAndWait()
            url = "https://chat.openai.com/chat"
            print('Starting up your Browser...')
            web.open(url)

        elif 'who' in userA:
            p = userA.replace('who', '')
            info = wiki.summary(p, 3)
            print(info)
            speak(info)
            E.runAndWait()

        elif 'what' in userA:
            person = userA.replace('what is', '')
            info = wiki.summary(person, 3)
            print(info)
            speak(info)
            E.runAndWait()

        elif 'where' in userA:
            pr = userA.replace('where ', '')
            info = wiki.summary(pr, 2)
            print(info)
            speak(info)
            E.runAndWait()

        elif 'how' in userA:
            person = userA.replace('how many', '')
            howw = wiki.summary(person, 1)
            print(howw)
            speak(howw)
            E.runAndWait()

        elif 'fact' in userA:
            speak("")
            E.runAndWait()

        elif 'your website' in userA:
            web.open_new_tab('https://www.jarvisinvest.com/')
            print('opening. .....')
            speak('opening My website .....')
            speak('Here it is !  ')
            E.runAndWait()

        elif 'toss' in userA:

            Tsdo = random.choice(toss)
            # print(Tsdo+" wins")
            speak(Tsdo+" wins")
            E.runAndWait()

        elif 'unwell' in userA:
            E.runAndWait()
            speak("Here are some clinics nearby:-")
            E.runAndWait()
            web.open("https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&eliflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzelifCC4QsQMyBQgAELEDMggIABCxAxCDATelifCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz")
            E.runAndWait()

        elif 'nice' in userA:
            speak("Thank you for your compliment sir. It matters a lot!")
            E.runAndWait()

        elif 'riddle' in userA:
            N = random.choice(M)
            print(N)
            speak(N)
            speak('Think for it ')
            E.runAndWait()
        elif 'physician' in userA:
            speak("Finding physicians nearby!")
            E.runAndWait()
            web.open("https://www.google.com/search?q=physician+near+me&source=hp&ei=zSWeYLnbMOvez7sPzquDoAU&iflsig=AINFCbYAAAAAYJ4z3UFbnwhwH1S2PB7uUkji0QVngyS6&oq=physicians+&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQyQMQCjIFCAAQkgMyBQgAEJIDMgIIADIHCAAQsQMQCjIECAAQCjICCAAyAggAMgIIADIHCAAQsQMQCjoICAAQsQMQgwE6CAguELEDEIMBOgUIABCxAzoICAAQsQMQyQM6BQguELEDUOIEWJMWYOsnaABwAHgAgAGvAYgBhg6SAQQwLjExmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz")

        elif 'Google' in userA:
            speak("Opening google for you!")
            E.runAndWait()
            web.open('www.google.com')
        elif 'introduce' in userA:
            speak("I am a intelligent system known as Jarvis")
            speak("I can do anything for you ")
            speak("if you want to visit my website, Then you can give me command as, open your website")
            E.runAndWait()

        elif 'YouTube' in userA:
            speak("Opening youtube for you!")
            E.runAndWait()
            web.open('youtube.com')

        elif 'hi' in userA:
            greet = random.choice(greets)
            speak(greet)
            E.runAndWait()

        elif 'bye' in userA:
            speak('bye')
            print("Bye!")
            E.runAndWait()


        elif 'news' in userA:
            speak("Opening some latest news for you sir!")
            E.runAndWait()
            web.open('chrome')
            web.open_new_tab("https://www.indiatoday.in/india")

        elif 'stopwatch' in userA:

            speak("opening a stopwatch. .")
            E.runAndWait()

            class Countdown(tk.Frame):

                def __init__(self, master):
                    super().__init__(master)
                    self.create_widgets()
                    self.show_widgets()
                    self.seconds_left = 0
                    self._timer_on = False

                def show_widgets(self):

                    self.label.pack()
                    self.entry.pack()
                    self.start.pack()

                def create_widgets(self):

                    self.label = tk.Label(self, text="00:00:00")
                    self.entry = tk.Entry(self, justify='center')
                    self.entry.focus_set()
                    self.start = tk.Button(self, text="Start",
                                        command=self.start_button)

                def countdown(self):
                    '''Update label based on the time left.'''
                    self.label['text'] = self.convert_seconds_left_to_time()

                    if self.seconds_left:
                        self.seconds_left -= 1
                        self._timer_on = self.after(1000, self.countdown)
                    else:
                        self._timer_on = False

                def start_button(self):
                    '''Start counting down.'''
                    # 1. to fetch the seconds
                    self.seconds_left = int(self.entry.get())
                    # 2. to prevent having multiple
                    self.stop_timer()
                    #    timers at once
                    self.countdown()

                def stop_timer(self):
                    '''Stops after schedule from executing.'''
                    if self._timer_on:
                        self.after_cancel(self._timer_on)
                        self._timer_on = False

                def convert_seconds_left_to_time(self):

                    return datetime.timedelta(seconds=self.seconds_left)

            if __name__ == '__main__':
                root = tk.Tk()
                root.resizable(False, False)

                countdown = Countdown(root)
                countdown.pack()

                root.mainloop()

        elif 'awesome' in userA:
            speak("My pleasure sir!")
            E.runAndWait()

        elif 'created you' in userA:
            speak("Its none other than you!")
            E.runAndWait()

        elif 'how are you' in userA:
            speak("I am awesome, and ready to take down your commands .")
            print("I am awesome, and ready to take down your commands .")
            E.runAndWait()

        elif 'team website' in userA:
            speak("Opening the team website for you sir!")
            web.open_new_tab(
                "https://sites.google.com/d/1h31McjWEGCNP6i1LsSCty-Knowi_QK9w/p/1nmiVG4V6SdncFPqh771Vj99NDRQGa9XE/edit")
            E.runAndWait()

        elif 'respond' in userA:
            speak("At your service sir!")
            E.runAndWait()

        elif 'timetable' in userA:
            speak("You have to get up at 7 3o, brush and get to breakfast. After that you have your breakfast and then you go for the school assignments given.. Then you have lunch and go play game. After completing it you go for the JARVIS conference and after that, watch Tv. That is how your schedule looks today sir")
            E.runAndWait()

        elif 'shutdown' in userA:
            speak("shuting down your pc. ")
            os.system("shutdown s \ t  1")
            break

        elif 'sleep' in userA:
            speak("Your pc will now sleep ")
            os.system("sleep /s /t 1")
            break

        elif 'alarm' in userA:

            speak("Type here for what do you want Alarm? ")
            E.runAndWait()
            act = str(input("for what do you want Alarm? :- "))
            speak("Type the time! ")
            E.runAndWait()
            Alarm = input("Enter the time:- ")
            print("Alarm has been set for ", Alarm)
            speak(Alarm)
            E.runAndWait()

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M")

                if now == Alarm:
                    print("time for ", act)
                    speak(act)
                    E.runAndWait()
                    play(r"C:\\Rigved\\python\\Python sounds. JARVIS\\Alarm.mp3")

                elif now > Alarm:
                    break

        elif 'images' in userA:
            web.open_new_tab("Hd images")
            web.open("chrome")
            speak("displaing image")
            E.runAndWait()
            print("opening . . .")

        elif 'cube' in userA:
            speak("opening Cube stopwatch for you")
            E.runAndWait()
            print("opening. ...")
            web.open_new_tab("https://cstimer.net/")


        elif 'reapeat' in userA:
            speak(userA)
            E.runAndWait()                

    except speech.UnknownValueError:
      speak("Could not understand audio")
    except speech.RequestError as e:
        speak("Sorry, there is no such feature here, work in progress")
    except KeyboardInterrupt:
        break
