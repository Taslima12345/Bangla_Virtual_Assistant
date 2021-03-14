import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
import pyttsx3
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import time
import subprocess
import psutil
import osascript
import wolframalpha
import json
import requests
import easygui 
import autopy
from pynput.keyboard import Key, Listener
import pyautogui
import pywhatkit
import random
import smtplib
from playsound import playsound
from os import path



#print('Tomar bektigoto Sohokari chalu hocche')
#print('Loading your AI personal assistant - G One')

# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def translate_To_Bangla(englis_text):
    translator = google_translator()
    bangla_text = translator.translate(englis_text, lang_src='en', lang_tgt='bn')   
    convert_to_aduio(bangla_text)


def play_audio(path_of_audio):
    playsound(path_of_audio)


def convert_to_aduio(translate_text):
    language = 'bn'
    myobj = gTTS(text=translate_text, lang=language, slow=False)
    myobj.save("voice.mp3") 
    play_audio('voice.mp3')

    os.remove('voice.mp3')

def convert_to_aduio_in_Eng(translate_text):
    language = 'en'
    myobj = gTTS(text=translate_text, lang=language, slow=False)
    myobj.save("voice2.mp3") 
    play_audio('voice2.mp3')

    os.remove('voice2.mp3')


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:

        speak1 = "Good Morning"
        translate_To_Bangla(speak1)
       # print("Shuprovat")
    elif hour>=12 and hour<18:
       # speak("Hello,Good Afternoon")
        speak2 = "Good Afternoon"
        translate_To_Bangla(speak2)
        # print("Shuvo Dupur")
    else:
        speak3 = "Good evening"
        translate_To_Bangla(speak3)


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='En-in')
           # print(f"user said:{statement}\n")

        except Exception as _:
            speak4 = "Pardon me, please say that again"
            translate_To_Bangla(speak4)
            return "None"
        return statement

speak5 = "Your personal Bangla Sohokari is being launched "
translate_To_Bangla(speak5)
wishMe()


if __name__=='__main__':


    while True:
        speak6 = ("Tell me how can I help you now?")

        translate_To_Bangla(speak6)
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "thamo" in statement or "bye" in statement or "stop" in statement:
            speak7 = ('Good bye')
            translate_To_Bangla(speak7)
            #print('your personal assistant G-one is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak8 = ("According to Wikipedia")
            translate_To_Bangla(speak8)
            #print(results)
            speak9 = results
            convert_to_aduio_in_Eng(speak9)


        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak10 = "youtube is open now"
            translate_To_Bangla(speak10)
            time.sleep(5)


        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak11= "Google chrome is open now"
            translate_To_Bangla(speak11)
            time.sleep(5)
        
        elif 'cpu' in statement:
            cpu_per = (psutil.cpu_percent())
            mem_details = (psutil.virtual_memory())
           # speak12 = ("CPU Utilization's  : " )+ str (cpu_per) + "\n Virtual Memory : " + str(mem_details))
            speak12 = "CPU Utilization's : "
            translate_To_Bangla(speak12)
            speak13 = str (cpu_per)
            convert_to_aduio_in_Eng(speak13)
            speak14= "Virtual Memory : "
            translate_To_Bangla(speak14)
            speak15 = str(mem_details)
            convert_to_aduio_in_Eng(speak15)
            
            #print ("CPU Utilization's Percentage is : " + str (cpu_per) + "\n Virtual Memory Detail's are : " + str(mem_details))
            time.sleep(5)

        elif 'gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak13 = "Google Mail open now"
            translate_To_Bangla(speak13)
            time.sleep(5)


        elif 'file' in statement or 'file explorer' in statement: 
           # subprocess.Popen(r'explorer /select,"C:\Program Files"')
           file = easygui.fileopenbox() #(take in the exact location where this file is located)

        # elif 'volume baraw' in statement or 'baraw' in statement:
        #     print(osascript.osascript("output volume of (get volume settings) & output muted of (get volume settings)"))

        elif 'Screenshot' in statement or 'screen' in statement:
            

            now = datetime.datetime.now()
            timenow = now.strftime("%H_%M_%S")

            filePath = path.join (path.dirname(path.abspath(__file__)), 'ScreenShots', str(datetime.date.today()))
            fileName = timenow+'.png'
            myss = pyautogui.screenshot()
            try:
                myss.save(path.join(filePath, fileName))
            except FileNotFoundError:
                os.mkdir(filePath)
                myss.save(path.join(filePath,fileName))     

            print("Done")
        
          
            
        elif "weather" in statement or "temperature" in statement or "abohawa" in statement or "tapmatra" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak10 = ("What's the city name")
            translate_To_Bangla(speak10)
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                details_weather =(" Temperature in kelvin unit  \n" +  str(current_temperature) + "And humidity  is " + str(current_humidiy) + " percentage" + 
                "\n description  " +str(weather_description) )
  
                translate_To_Bangla(details_weather)
                
            else:
                speak14 = (" City Not Found ")
                translate_To_Bangla(speak11)


        elif 'time' in statement or 'somoy' in statement or 'KoiTa' in statement or 'Kota' in statement:
           
            dayDate = datetime.datetime.now().strftime("%a, %b %d, %Y")
            speak_date= ("Today is")
            speak_date2 =f"{dayDate}"
            # print(f"Today is {dayDate}")
            translate_To_Bangla(speak_date)
            convert_to_aduio(speak_date2)

            currTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak_time = (f"and the time is {currTime}")
            translate_To_Bangla(speak_time)
            print(speak_time)


        elif "overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/users/login")
            speak17 = ("Here is stackoverflow")
            translate_To_Bangla(speak17
            )
        elif 'news' in statement :
            news = webbrowser.open_new_tab("https://www.prothomalo.com/")
            speak18 = ('Here are some headlines from the Prothom Alo')
            translate_To_Bangla(speak18)
            time.sleep(6)

        # elif "camera" in statement or "take a photo" in statement:
        #     ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        # elif 'ask' in statement:
        #     speak('I can answer to computational and geographical questions and what question do you want to ask now')
        #     question=takeCommand()
        #     app_id="R2K75H-7ELALHR35X"
        #     client = wolframalpha.Client('R2K75H-7ELALHR35X')
        #     res = client.query(question)
        #     answer = next(res.results).text
        #     speak(answer)
        #     print(answer)


        elif "shutdown" in statement or "shut down" in statement:
            speak19 = ("Ok , your pc will shutting down in 10 second make sure you exit from all applications")
            translate_To_Bangla(speak19)
            subprocess.call(["shutdown", "/s"])
            time.sleep(3)

        elif "restart" in statement or "re start" in statement:
            speak20 = ("Ok , your pc will restart in 10 second make sure you exit from all applications")
            translate_To_Bangla(speak20)
            #subprocess.call(["shutdown", "/r "])
            os.system("shutdown /r")
            time.sleep(3)

        elif 'gan' in statement or 'gaan' in statement :
            songName = statement.replace('gan', ' ')
            speak21 =   ("The song is being played")   
            translate_To_Bangla(speak21)   
            #print('playing ' + songName)
            pywhatkit.playonyt(songName)

        elif 'music' in statement:
            music_dir = "C:\\Users\\User\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "log off" in statement or "sign out" in statement:
            speak22 = ("Ok , your pc will log off in 10 second make sure you exit from all applications")
            translate_To_Bangla(speak22)
            subprocess.call(["shutdown", "/l"])
            time.sleep(3)
