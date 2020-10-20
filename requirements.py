import pyttsx3
import os
import datetime
import time
import wikipedia
import webbrowser
import PyPDF2
from words import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voice", voices[0].id)


# The speak function
def speak(audio):
    # time.sleep(2)
    engine.say(audio)
    engine.runAndWait()


# Greeting
def Greet():
    nm = input(">> What is your name: ")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning {nm}")
        # input(">> Good morning")
    elif hour >= 12 and hour <= 18:
        speak(f"Good afternoon {nm}")
        # input(">> Good afternoon")
    else:
        speak(f"Good evening {nm}")


def wiking():
    sentenc = input(f">> What do you want to search on wikipedia: ")
    sentenc += " Wikipedia"
    nl = int(input(">> Enter no. of sentences: "))
    l = wikipedia.summary(sentenc, sentences=nl)
    print(l)
    speak(l)


def webs():
    o = input(">> Which website do you want to search: ")
    webbrowser.open_new(f"https://{o}")
    speak(f"Opening {o}")


def code():
    path = "C:\\Users\\Your_Usrename\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
    os.startfile(path)


def pdf():
    a = PyPDF2.PdfFileReader("Python1.pdf")
    # print(a.documentInfo)
    # speak(a.documentInfo)
    # speak(a.getNumPages())
    speak(a.getPage(100).extractText())


def say():
    p = input("Enter the text: ")
    speak(p)


def tables():
    tables = []
    no = int(input(">> The table of which number do you want to know: "))
    for x in range(10):
        tables.append(x * no)

    print(tables)


def timefy():
    hr = int(datetime.datetime.now().hour)
    mn = int(datetime.datetime.now().minute)
    sc = int(datetime.datetime.now().second)
    time = f"{hr}:{mn}:{sc}"
    print(time)
    speak(time)

timefy()