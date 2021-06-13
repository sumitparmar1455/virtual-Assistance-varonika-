import pyttsx3
import datetime
import webbrowser
import pyaudio
import os
import time
import random
import subprocess
import pywhatkit
import pyautogui
import sys
import winshell
import psutil
import speedtest
import PyPDF2
import requests
import ctypes
import platform
import wikipedia
import openpyxl
import pyjokes
import wmi
from pywinauto.application import Application
from pywikihow import search_wikihow
from selenium import webdriver
import screen_brightness_control as sbc
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('volume',0.90)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning..........")
        strtime = datetime.datetime.now().strftime("%H:%M")
        speak(f"it is {strtime}")
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "junagadh"
        API_KEY = "98bb246f4a4889ec93b07854e388e1d7"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            report = data['weather']
            speak(f" Temperature  is: {temperature}")
            speak(f" weather is : {report[0]['description']}")


    elif hour>=12 and hour<18:
        speak("Good Afternoon................")
        strtime = datetime.datetime.now().strftime("%H:%M")
        speak(f"it is {strtime}")
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "junagadh"
        API_KEY = "98bb246f4a4889ec93b07854e388e1d7"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            report = data['weather']
            speak(f" Temperature  is: {temperature}")
            speak(f" weather is : {report[0]['description']}")

    else:
        speak("Good Evening.................")
        strtime = datetime.datetime.now().strftime("%H:%M")
        speak(f"it is {strtime}")
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "junagadh"
        API_KEY = "98bb246f4a4889ec93b07854e388e1d7"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            report = data['weather']
            speak(f" Temperature  is: {temperature}")
            speak(f" weather is : {report[0]['description']}")

    speak("i am veronica")
    speak("design and programming by sumit parmar ")
    speak("tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("i listening .........................")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("i recognizing ..........................")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        speak("network connection Error")
        speak("unable to recognize your voice")
        return 'None'
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        ########################### CODING TO BUILDING  LOGIC FOR PERFORM TASK ##################################################3333
        #code for open and search something in website
        if'open google'in query:
            speak("sure boss................")
            speak("command is accept...........")
            speak("google is opening .................")
            webbrowser.open_new_tab('https:\\www.google.com')

        elif'search on google' in query:
            speak("sure boss.................")
            speak("command is accept..................")
            speak("what do you want to search in google")
            search = takecommand()
            speak("i search on google According to you say")
            webbrowser.open(f"{search}")
            speak("boss results is done")

         #code for search and play music in youtube
        elif'search on youtube'in query:
            speak("sure boss...............")
            speak("command is accepet...............")
            speak("are you want to search in youtube")
            replay = takecommand()
            if'yes'in replay:
                speak("tell me what is search in youtube")
                search = takecommand()
                speak("ok boss....................")
                speak("i search on youtube according to say")
                pywhatkit.playonyt(f"{search}")
                speak("boss result is done")

          # WORK ON PLAY SONG ON YOUTUBE###########
        elif'play song on youtube' in query:
            speak("sure boss.............")
            speak("command is accepet..................")
            speak("are you want to play song on youtube.....")
            replay = takecommand()
            if'yes'in replay:
                speak("which song i play in youtube")
                song = takecommand()
                speak("ok boss............")
                speak("i play a song on youtube according to say")
                pywhatkit.playonyt(f"{song}")
                speak("boss song is playing on youtube")

           ##### PLAY JOKES ON YOUTUBE###########3
        elif'play jokes on youtube'in query:
            speak("sure boss.......................")
            speak("command is accepet................................")
            speak("are you listen jokes on youtube")
            replay = takecommand()
            if'yes'in replay:
                speak("which  jokes i play on youtube")
                jokes = takecommand()
                speak("ok boss........................")
                speak("i play a jokes on youtube according to say")
                pywhatkit.playonyt(f"{jokes}")
                speak("boss jokes is playing on youtube")

         #######PLAU MOVIE ON YOUTUBE #########
        elif'play movie on youtube'in query:
            speak("sure boss")
            speak("command is accepet.............")
            speak("are you want to see movie on youtube")
            replay = takecommand()
            if'yes'in replay:
                speak("which movie i play on youtube")
                movie = takecommand()
                speak("ok boss")
                speak("i play a movie on youtube according to say")
                pywhatkit.playonyt(f"{movie}")
                speak("boss movies is playing on youtube")

        elif'open youtube' in query:
            speak("sure boss")
            speak("command is accept...........")
            speak("youtube is opening .................")
            webbrowser.open_new_tab("https:\\www.youtube.com")

        elif'open firefox'in query:
            speak("sure boss..............................")
            speak("command is accepet.....................")
            speak("fire fox is opening.......................")
            codepath = "C:Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codepath)

        elif'open facebook'in query:
            speak("sure boss..............")
            speak("command is accept...........")
            speak("facebook is opening.............")
            webbrowser.open_new_tab("https:\\www.facebook.com")

        elif'open instagram'in query:
            speak("sure boss.................")
            speak("command is accept........")
            speak("instagram is opening................")
            webbrowser.open_new_tab("https:\\www.instagram.com")

        elif'open twitter'in query:
            speak("sure boss....................")
            speak("command is accepet.................")
            speak("twitter is opening")
            webbrowser.open_new_tab("https:\\www.twitter.com")

        elif'open amazon'in query:
            speak("sure boss")
            speak("command is accepet............")
            speak("amazon is opening now")
            webbrowser.open_new_tab("https:\\www.amazon.com")

       ############## CLOSING THE ALL WEBSITE##########3
        elif'close google'in query:
            speak("sure boss................")
            speak("command is accepet....................")
            speak("boss google is closing")
            os.system("TASKKILL /F /IM chrome.exe")

        elif'close firefox'in query:
            speak("sure boss................")
            speak("command is accepet...........................")
            speak("fire fox is closing..................")
            os.system("TASKKILL /F /IM firefox.exe")

         ##################### WORK ON GMAIL  #############
        elif'open gmail'in query:
            speak("sure boss")
            speak("command is accepet...........................")
            webbrowser.open_new_tab("https:\\www.gmail.com")

            ############# WORK ON GMAIL ###########################
            ##################### LOGIN #################3
        elif'login in gmail' in query:
            speak("sure boss")
            speak("command is accepet..................")
            driver = webdriver.Chrome()
            driver.get("https:\\www.gmail.com")
            speak("boss gmail login page is opening")
            time.sleep(1)
            speak("i automatically enter your gmail id")
            driver.find_element_by_name("identifier").send_keys("sumit.parmar@ngivbt.edu.in")
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
            driver.implicitly_wait(4)
            speak("i automatically enter your gmail password")
            driver.find_element_by_name("password").send_keys("ngivbt@123")
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
            speak("boss login in gmail is done")

        elif'check mail in gmail'in query:
            speak("sure boss")
            speak("command is accepet...............")
            speak("first i login in your gmail account and then i automatically check mail in gmail")
            driver = webdriver.Chrome()
            driver.get("https:\\www.gmail.com")
            speak("gmail login page is opening................")
            time.sleep(1)
            driver.find_element_by_name("identifier").send_keys("sumit.parmar@ngivbt.edu.in")
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
            driver.implicitly_wait(4)
            driver.find_element_by_name("password").send_keys("ngivbt@123")
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
            speak("boss here you can see your mail in inbox")

          ########################WORK IN GOOGLE CLASSROOM AND GOOGLE MEET #####################
          ############################  WORK
        elif'login in classroom'in query:
            speak("sure boss")
            speak("command is accepet.................")
            speak("i automatically login in your google classroom account")
            driver = webdriver.Chrome()
            driver.get("https://edu.google.com/products/classroom/")
            speak("google classroom login page is opening...............")
            driver.implicitly_wait(4)
            driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            speak("i automatically enter your gmail id")
            driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("sumit.parmar@ngivbt.edu.in")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
            speak("i automatically enter your gmail password..............")
            driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("ngivbt@123")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
            speak("boss login in google classroom is done")

        elif'check class work in classroom'in query:
            speak("sure boss")
            speak("command is accepet.............")
            speak("first i login in your google classroom account and then i check classwork in classroom")
            driver = webdriver.Chrome()
            driver.get("https://edu.google.com/products/classroom/")
            speak("google classroom login page is opening.................")
            driver.implicitly_wait(4)
            driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("sumit.parmar@ngivbt.edu.in")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
            driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("ngivbt@123")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]').click()
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/nav/div[2]/div/div[2]/a').click()
            speak("here you can see your classwork")

            ################################## WORK IN LOGIN IN WEB SITE LIKE FACEBOOK ,INSTAGRAM
        elif'login in facebook'in query:
            speak("sure boss................")
            speak("command is accepet...............")
            speak("i automatically login in your facebook account")
            driver = webdriver.Chrome()
            driver.get("https:\\www.facebook.com")
            driver.maximize_window()
            speak("facebook login page is opening............")
            driver.implicitly_wait(4)
            speak("i automatically enter your facebook id")
            email = driver.find_element_by_xpath('//*[@id="email"]')
            email.send_keys('9328228033')
            speak("i automatically enter your facebook password")
            password = driver.find_element_by_xpath('//*[@id="pass"]')
            password.send_keys('sumitparmar1455')
            driver.find_element_by_xpath( '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
            pyautogui.press("enter")
            print("login in facebook is successfully")

        elif'login in linkedin'in query:
            speak("sure boss")
            speak("command is accepet...........")
            speak("i automatically login in your instagram account")
            driver = webdriver.Chrome()
            driver.get("https:\\www.linkedin.com")
            speak("boss linkedin login page is opening.........")
            driver.maximize_window()
            time.sleep(1)
            speak("i automatically enter your linkedin email id")
            email = driver.find_element_by_xpath('//*[@id="session_key"]')
            email.send_keys('9328228033')
            speak("i automatically enter your  linkedin password")
            password = driver.find_element_by_xpath('//*[@id="session_password"]')
            password.send_keys('sumit123')
            driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button')
            pyautogui.press("enter")
            speak("login in linkedin account is successfully")

        elif'login in instagram'in query:
            speak("sure boss")
            speak("command is accepet............")
            speak("i automatically login in your instagram account")
            driver = webdriver.Chrome()
            driver.get("https:\\www.instagram.com ")
            speak("instagram login page is opening..............")
            driver.maximize_window()
            driver.implicitly_wait(4)
            speak("i automatically enter your instagram id")
            email = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            email.send_keys('sumitparmar5500@gmail.com')
            speak("i automatically enter your Instagram password")
            password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys('sumit123')
            driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
            speak("boss login in instagram is done")

        elif'login in twitter'in query:
            speak("sure boss")
            speak("command is accepet......................")
            speak("i automatically login in your twitter account")
            driver = webdriver.Chrome()
            driver.get('https://twitter.com/login')
            speak("twitter login page is opening..............")
            driver.maximize_window()
            driver.implicitly_wait(4)
            print("i automatically enter your twitter id")
            email = driver.find_element_by_xpath( '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            email.send_keys('@sumitpa07645254')
            print("i automatically enter your twitter password")
            password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password.send_keys('sumitparmar1455')
            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
            pyautogui.press("enter")
            print("login in twitter account is successfully")

          #code for opening useful web site
          #code for open stackoverflow
        elif'open stackoverflow'in query:
            speak("sure boss......................")
            speak("command is accepet...................")
            speak("stackoverflow is opening.......................")
            webbrowser.open_new_tab("https://stackoverflow.com/")

          #code for search stackoverflow
        elif'open W3 school'in query:
            speak("sure boss...................")
            speak("command is accept......")
            webbrowser.open_new_tab("https://www.w3schools.com/")

          #code for open google meet
        elif'open google meet'in query:
            speak("sure boss.............................")
            speak("command is accepet............................")
            speak("google meet is opening......................")
            webbrowser.open_new_tab("https://meet.google.com/")

          #code for open google classroom
        elif'open classroom'in query:
            speak("sure boss....................")
            speak("command is accepet..........................")
            speak("google classroom is opening.....................")
            webbrowser.open_new_tab("https://classroom.google.com/h")

          #code for search wikipedia and searching something in wikimedia
         #code for wikipedia
        elif'wikipedia'in query:
            speak("sure boss................")
            speak("command is accepet....................")
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=20000)
            speak("according to wikipedia")
            print(results)
            speak(results)

         #code for open and close windows application
         ###################### WORK ON  VISUAL STUDIO CODE #######################3
        elif'open code'in query:
            speak("sure boss.................")
            speak("command is accept...................")
            speak("are you want to open Visual Studio Code IDE ")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in code ")
                work = takecommand()
                speak("ok boss.................")
                speak("Visual Studio Code IDE is opening ............................")
                codepath = "C:\\Users\\sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

        elif'close code'in query:
            speak("sure boss................")
            speak("command is accept............")
            speak("boss Visual Studio Code IDE is closing now")
            os.system("TASKKILL /F /IM code.exe")


              ################ WORK ON INTELLIJ IDEA COMMUNITY EDITION ##########################
        elif'open java IDE'in query:
            speak("sure boss........................")
            speak("command is accepet.........................")
            speak("are you want to open IntelliJ IDEA Community Edition 2020.2.3")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in IntelliJ IDEA Community Edition 2020.2.3 ")
                work = takecommand()
                speak("ok boss..................")
                speak("IntelliJ IDEA Community Edition 2020.2.3 is opening................")
                codepath = "C:\\Program Files\\JetBrains\IntelliJ IDEA Community Edition 2020.2.3\\bin\\idea64.exe"
                os.startfile(codepath)

        elif'close java IDE'in query:
            speak("sure boss................")
            speak("command is accepet..................")
            speak("IntelliJ IDEA Community Edition 2020.2.3 is closing now")
            os.system("TASKKILL /F /IM idea64.exe")

                #########################3 WORK IN ANDROID STUDIO ##############
        elif'open android studio'in query:
            speak("sure boss")
            speak("command is accepet.................")
            speak("are you want to open android studio")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in android studio ")
                work = takecommand()
                speak("ok boss..................")
                speak("android studio is opening...............")
                codepath = ""
                os.startfile(codepath)

        elif'close android studio'in query:
            speak("sure boss...............")
            speak("command is accepet...................")
            speak("android studio is closing...................")

               ###################3 WORK ON SUBLIME IDE #############################3
        elif'open sublime' in query:
            speak("sure boss...........")
            speak("command is accept.................")
            speak("are you want to open  Sublime Text 3 IDE")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in  Sublime Text 3 IDE")
                work = takecommand()
                speak("ok boss..................")
                speak("Sublime Text 3 IDE is opening ")
                codepath = "C:\\Program Files (x86)\\Sublime Text 3\\sublime_text.exe"
                os.startfile(codepath)

        elif'close sublime'in query:
            speak("sure boss")
            speak("command is accept...................")
            speak("boss sublime ide is closing now")
            os.system("TASKKILL /F /IM sublime_text.exe")

                   ################# WORK ON NOTEPAD ###################
        elif'open notepad'in query:
            speak("sure boss...............")
            speak("command is accept.......")
            speak("are you want to open notepad++")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in notepad")
                work = takecommand()
                speak("ok boss")
                speak("notepad++ is opening ")
                codepath ="C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(codepath)

        elif'close notepad' in query:
            speak("sure boss........")
            speak("command is accepet...........")
            speak("boss notepad is closing ")
            os.system("TASKKILL /F /IM notepad++.exe")

              ####################### WORK ON ADOBE DREAMWEAVER 2020 #####################
        elif'open editor'in query:
            speak("sure boss...............")
            speak("command is accepet..............")
            speak("are you want to open Adobe Dreamweaver 2020")
            replay =takecommand()
            if'yes'in replay:
                speak("which work do you want in Adobe Dreamweaver 2020")
                work = takecommand()
                speak("ok boss......")
                speak("Adobe Dreamweaver 2020 is opening")
                codepath = "C:\\Program Files\\Adobe\\Adobe Dreamweaver 2020\\Dreamweaver.exe"
                os.startfile(codepath)

        elif'close editor'in query:
            speak("sure boss................")
            speak("command us accepet.......................")
            speak("Adobe Dreamweaver 2020 is closing")
            os.system("TASKKILL /F /IM Dreamweaver.exe")

           #################### WORK ON PICASA ##########################33
        elif'open picasa'in query:
            speak("sure boss.........................")
            speak("command is accepet......................")
            speak("are you want to open picasa3 editor")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in picasa3")
                work = takecommand()
                speak("ok boss")
                speak("picasa3 editor is opening")
                codepath = "C:\\Program Files (x86)\\Google\\Picasa3\\Picasa3.exe"
                os.startfile(codepath)

        elif'close picasa'in query:
            speak("sure boss........")
            speak("command is accept")
            speak("boss picasa3 is closing")
            os.system("TASKKILL /F /IM Picasa3.exe")

                  ##############3 WORK ON PHOTOSHOP ######################33
        elif'open photoshop'in query:
            speak("sure boss..................")
            speak("command is accepet...................")
            speak("are you want to open Adobe Photoshop CS6 ")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in Adobe Photoshop CS6")
                work = takecommand()
                speak("ok boss")
                speak("Adobe Photoshop CS6 is opening .....................")
                codepath = "C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe"
                os.startfile(codepath)

        elif'close photoshop'in query:
            speak("sure boss................")
            speak("command is accepet..............")
            speak("Adobe Photoshop CS6 is closing")
            os.system("TASKKILL /F /IM Photoshop.exe")

                   ############################### WORK ON WINDOWS PROGRAMS ############3
           #code for open and close windows application
        #code for open cmd
        elif'open command prompt'in query:
            speak("sure boss.................")
            speak("command is accepet...............")
            speak("command prompt is opening..............")
            os.system('start cmd')

        elif'close command prompt' in query:
            speak("sure boss...............")
            speak("command us accepet...................")
            speak("command prompt is closing..................")
            os.system("TASKKILL /F /IM cmd.exe")

         #code for open task manager
        elif'open task manager'in query:
            speak("sure boss......................")
            speak("command is accepet......................")
            speak('task manager is opening..................')
            os.system('start taskmgr')

        elif'close task manager'in query:
            speak("sure boss.................")
            speak("command is accepet.................")
            speak("task manager is closing............")
            os.system("TASKKILL /F /IM Taskmgr.exe")

          ############### WORK FOR OPENING SETTING
        elif'open amd setting'in query:
            speak("sure boss...........")
            speak("command  is accepet............")
            speak("are you want to opening amd setting")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                codepath = "C:\\Program Files\\AMD\\CNext\\CNext\\RadonSettings.exe"
                speak("boss AMD setting is opening now")
                os.startfile(codepath)

         #################### WORK IN SETTING SECTION #############3
        elif'open background setting'in query:
            speak("sure boss")
            speak("command is accepet...........")
            speak("are you want to opening background setting")
            replay = takecommand()
            if'yes'in replay:
                speak("back ground setting is opening...........")
                os.system("start ms-settings:personalization-background")
                speak("here you can see background setting")

        elif'open sound setting' in query:
            speak("sure boss")
            speak("command is accepet...............")
            speak("are you want to opening sound setting")
            replay = takecommand()
            if'yes'in replay:
                speak("sound setting is opening.............")
                os.system("start ms-settings:sound")
                speak("here you can see sound setting")

        elif'open theme setting'in query:
            speak("sure boss")
            speak("command is accepet...............")
            speak("are you want to opening theme setting")
            replay = takecommand()
            if'yes'in replay:
                speak("theme setting is opening...........")
                os.system("start ms-settings:themes ")
                speak("here you can see theme setting.......")

        elif'open bluetooth setting'in query:
            speak("sure boss")
            speak("command is accepet...............")
            speak("are you want to opening bluetooth setting")
            replay = takecommand()
            if 'yes' in replay:
                speak("bluetooth setting is opening..............")
                os.system("start ms-settings:bluetooth")
                speak("here you can see bluetooth setting")

        elif'check window update' in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("are you want to check window update")
            replay = takecommand()
            if'yes'in replay:
                speak("i automatically check windows update")
                os.system("start  ms-settings:windowsupdate-action ")
                speak("here you can see windows update")

        elif'check window update history'in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("are you want to opening check windows update history")
            replay = takecommand()
            if'yes'in replay:
                speak("i automatically check windows update history")
                os.system("start ms-settings:windowsupdate-history ")
                speak("here you can see windows update history")

        elif'check storage in system'in query:
            speak("sure boss..................")
            speak("command is accepet................")
            speak("are you want to check storage in system")
            replay = takecommand()
            if'yes'in replay:
                speak("i automatically check the storage in system")
                os.system("start ms-settings:storagesense")
                speak("here you can see the storage in system")

        ############################ WORK  OPENING AND CLOSING PPT##################

        #system information
          #code for show system information
        elif'check system information'in query:
            speak("sure boss...............")
            speak("command is accepet...................")
            speak("are you want to check system information")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.................")
                speak("wait a minute....................")
                speak("i automatically check the system.............")
                uname = platform.uname()
                speak(f"system is:-{uname.system}")
                speak(f"release is :-{uname.release}")
                speak(f"machine is:-{uname.machine}")
                speak(f"node is:-{uname.node}")
                speak(f"processor is :-{uname.processor}")
                speak(f"version is:-{uname.version}")
                speak("boss,checking system information successfully done")

            elif'check memory information' in query:
                speak("sure boss....................")
                speak("command is accepet....................")
                speak("are you want to check memory information")
                replay = takecommand()
                if 'yes' in replay:
                    speak("wait a minute..............")
                    speak("i check all memory information")
                    svmem = psutil.virtual_memory()
                    speak(f"total memory in the system is:{svmem.total} ")
                    speak(f"available memory  in the system is:{svmem.available}")
                    speak(f"used memory  in the system is:{svmem.used}")
                    speak(f"free memory in the system is{svmem.free}")
                    speak(f"percentage in the system memory is:{svmem.percent}% ")

         #code for create a folder
        elif'create a folder'in query:
           speak("sure boss.......................")
           speak("command is accepet..........................")
           speak("are you want to create a folder")
           replay = takecommand()
           if'yes'in replay:
               speak("ok boss....................")
               speak("tell me which place i make a folder")
               place = takecommand()
               if'desktop'in place:
                   speak("sure boss ")
                   speak("i make a folder in desktop")
                   path = "C:\\Users\\sumit\\Desktop\\new folder"
                   try:
                       os.mkdir(path)
                   except OSError:
                       speak("creation of the directory %s failed" % path)
                   else:
                       speak("successfully created the directory %s" % path)
                       speak("boss folder is create successfully")

         #code for create a sub folder
        elif'create a subfolder'in query:
            speak("sure boss.................")
            speak("command is accepet.......................")
            speak("are you want to create a subfolder.....................")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...........................")
                speak("i automatically create a subfolder.................")
                path = "C:\\Users\\sumit\\Desktop\\new folder\\new folder"
                try:
                    os.mkdir(path)
                except OSError:
                    speak("creation of the directory %s failed" % path)
                else:
                    speak("successfully created the directory %s" % path)
                    speak("boss subfolder is create successfully")

         #code for create a folder in subfolder
        elif'create a folder in subfolder'in query:
            speak("sure boss.............................")
            speak("command is accepet..........................")
            speak("are you want to create a folder in subfolder.......")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.....................")
                speak("i automatically create a folder in subfolder......................")
                path = "C:\\Users\\sumit\\Desktop\\new folder\\new folder\\new folder"
                try:
                    os.mkdir(path)
                except OSError:
                    speak("creation of the directory %s failed" % path)
                else:
                    speak("successfully created the directory %s" % path)
                    speak("boss folder is create in subfolder is successfully")

        #code for delete folder
        elif'delete a folder'in query:
            speak("sure boss...................")
            speak("command is accepet..............................")
            speak("are you want to delete a folder")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss....................")
                speak("i automatically delete a folder")
                path = "C:\\Users\\sumit\\Desktop\\new folder"
                try:
                    os.rmdir(path)
                except OSError:
                    speak("delete of the directory %s failed" % path)
                else:
                    speak("successfully delete the directory %s" % path)
                    speak("boss folder is delete successfully")

        #code for delete a subfolder
        elif'delete a subfolder'in query:
            speak("sure boss..........................")
            speak("sure boss...................")
            speak("command is accepet..............................")
            speak("are you want to delete a subfolder")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss....................")
                speak("i automatically delete a subfolder")
                path = "C:\\Users\\sumit\\Desktop\\new folder\\new folder"
                try:
                    os.rmdir(path)
                except OSError:
                    speak("delete of the directory %s failed" % path)
                else:
                    speak("successfully delete the directory %s" % path)
                    speak("boss  subfolder is delete successfully")

        #code for delete a folder in subfolder
        elif'delete a folder in subfolder'in query:
            speak("sure boss.........................")
            speak("sure boss...................")
            speak("command is accepet..............................")
            speak("are you want to delete a folder in subfolder")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss....................")
                speak("i automatically delete a folder in subfolder")
                path = "C:\\Users\\sumit\\Desktop\\new folder\\new folder\\new folder"
                try:
                    os.rmdir(path)
                except OSError:
                    speak("delete of the directory %s failed" % path)
                else:
                    speak("successfully delete the directory %s" % path)
                    speak("boss  folder delete in subfolder is  successfully")

        #code for rename the folder
        elif'rename the folder'in query:
            speak("sure boss.....................")
            speak("sure boss...................")
            speak("command is accepet..............................")
            speak("are you want to rename the folder")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss....................")
                speak("i automatically rename a folder")
                speak("tell me which name  to  given rename folder")
                rename = takecommand()
                speak("i rename the folder as you say")
                winshell.rename_file("C:\\Users\\sumit\\Desktop\\new folder", "C:\\Users\\sumit\\Desktop\\sumit")
                speak("successfully rename the new folder")

        #code for open and close microsoft office software
        #code for open and close word
        elif'open word'in query:
            speak("sure boss.................")
            speak("command is accept.............")
            speak("are you want to open microsoft office word ")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in microsoft office word")
                work = takecommand()
                speak("ok boss")
                codepath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                speak("boss microsoft office word is opening  ")
                os.startfile(codepath)

        elif'close word' in query:
            speak("sure boss.............................")
            speak("command is accept..........................")
            speak("boss microsoft office word is closing ")
            os.system("TASKKILL /F /IM WINWORD.exe")

        #code for open and close powerpoint
        elif'open powerpoint' in query:
            speak("sure boss")
            speak("command is accept......................")
            speak("are you want to open microsoft office powerpoint ")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in microsoft office powerpoint")
                work = takecommand()
                speak("ok boss")
                codepath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                speak("boss microsoft office powerpoint is opening ")
                os.startfile(codepath)

        elif'close powerpoint' in query:
            speak("sure boss..............")
            speak("command is accepet.............................")
            speak("boss microsoft office powerpoint is closing now")
            os.system("TASKKILL /F /IM POWERPNT.exe")

        #code for open and close excel
        elif'open excel'in query:
            speak("sure boss.......")
            speak("command is accepet...............")
            speak("are you want to open microsoft office excel ")
            replay = takecommand()
            if'yes'in replay:
                speak("which work do you want in microsoft office excel")
                work = takecommand()
                speak("ok boss")
                codepath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                speak("microsoft office excel is opening...............")
                os.startfile(codepath)

        elif'close excel'in query:
            speak("sure boss................")
            speak("command is accepet.............................")
            speak("microsoft office excel is closing now")
            os.system("TASKKILL /F /IM EXCEL.exe")

    #code for play music
        elif'play music'in query:
            speak("sure boss...............")
            speak("command is accept..............")
            speak("music is opening ")
            music_dir = "D:\\music\\all music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir,rd))

        #code for play next music
        elif'play next music'in query:
            speak("sure boss.......................")
            speak("command is accepet.....................")
            speak("next music is opening..................")
            music_dir = "D:\\music\\all music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir,rd))

        #code for change music
        elif'change music'in query:
            speak("sure boss...............")
            speak("command is accept.................")
            speak("music is change....................")
            music_dir = "D:\\music\\all music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))

         #code for playing favourite music
        elif'play your favourite music'in query:
            speak("sure boss....................")
            speak("command is accepet...........................")
            speak("are you want to play my favourite music")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..................")
                speak("i play my favourite music ")
                music_dir = "D:\\music\\new song of pandrive"
                speak("i enjoying to listening this music")
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))

        # code for play 2011 to 2020 music
        elif'play 2011 song' in query:
            speak("sure boss..............")
            speak("command is accepet.................")
            speak("are you want to listen 2011 song")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss")
                speak("i playing 2011 song ")
                speak("music is opening............")
                music_dir = "D:\\music\\listen\\2011"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("enjoy to listening 2011 song")

        elif'play 2012 song'in query:
            speak("sure boss..................")
            speak("command is accepet...............")
            speak("are you want to listen 2012 song")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("i playing 2012 song")
                music_dir = "D:\\music\\listen\\2012"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir,rd))
                speak("enjoy to listening 2012 song")

        elif'play 2013 song' in query:
            speak("sure boss......................")
            speak("command is accepet.........................")
            speak("are you want to listen 2013 song")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...............")
                speak("i playing 2013 song")
                music_dir = "D:\\music\\listen\\2013"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir,rd))
                speak("enjoying to listening 2013 song")

        elif'play 2014 song' in query:
            speak("sure boss..............")
            speak("command is accepet...............")
            speak("are you want to listen 2014 song")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..............")
                speak("i playing 2014 song")
                music_dir = "D:\\music\\listen\\2014"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir,rd))
                speak("enjoying to listening 2014 song")

        elif'play 2015 song'in query:
            speak("sure boss.......................")
            speak("command is accepet.......................")
            speak("are you want to listen 2015 song")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss..............")
                speak("i playing 2015 song")
                music_dir = "D:\\music\\listen\\2015"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("enjoying to listening 2015 song")

        elif'play 2016 song' in query:
            speak("sure boss.....................")
            speak("command is accepet...................")
            speak("are you want to listen 2016 song")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..............")
                speak("i playing 2016 song")
                music_dir = "D:\\music\\listen\\2016"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("enjoying to listening 2016 song")

        elif'play 2017 song' in query:
            speak("sure boss...................")
            speak("command is accepet..........................")
            speak("are you want to listen 2017 song")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss..............")
                speak("i playing 2017 song")
                music_dir = "D:\\music\\listen\\2016"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("enjoying to listening 2016 song")

        elif'play 2018 song' in query:
            speak("sure boss............................")
            speak("command is accepet............................")
            speak("are you want to listen 2018")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.......................")
                speak("i playing 2018 song")
                music_dir = "D:\\music\\listen\\2018"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
                print(songs)
                speak("enjoying to listening 2017 song")

        elif'play 2019 song' in query:
            speak("sure boss...................")
            speak("command us accepet....................")
            speak("are you want to listen 2019")
            replay = takecommand()
            if'yes'in replay:
                speak("sure boss.....................")
                speak("i playing 2019 song")
                music_dir = "D:\\music\\listen\\2016"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("enjoying to listening 2019 song")

        elif'play 2020 song'in query:
            speak("sure boss..................................")
            speak("command is accepet................................")
            speak("are you want to listen 2020 song")
            replay = takecommand()
            if'yes'in replay:
                speak("sure boss...........")
                speak("i playing 2020 song")
                music_dir = "D:\\music\\listen\\2016"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("enjoying to listening 2020 song")

            #code for play gujarati music
            elif'play gujarati music'in query:
                speak("sure boss...................")
                speak("command is accepet...................")
                speak("are you listen gujarati music")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss.................")
                    music_dir = "D:\\music\\listen\\ZAVERCHAND MEGHANI"
                    speak("enjoying to listen gujarati music")
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir,rd))

            #code for play punjabi music
            elif'play punjabi music'in query:
                speak("sure boss...................")
                speak("command is accept..................")
                speak("are you listen punjabi music")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss..........")
                    music_dir="D:\\music\\listen\\PUNJABI COLLECTION"
                    speak("enjoying to listen punjabi music")
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir,rd))

            #code for some relax music
            elif'play some relax music'in query:
                speak("sure boss............")
                speak('command is accepet...................')
                speak("would you like to listen some relax music")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss....................")
                    music_dir = "D:\\music\\relex song"
                    speak("enjoying to listen some relex music")
                    songs = os.listdir(music_dir)
                    print(songs)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir,rd))

            #code for play english music
            elif'play english music'in query:
                speak("sure boss")
                speak("command is accepet..............")
                speak("would you like to listen english music ")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss")
                    speak("enjoying to listen some english movie")
                    songs = os.listdir(music_dir)
                    print(songs)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir,rd))

            #code for play romantic music
            elif'play romantic music'in query:
                speak("sure boss..................")
                speak("command is accepet..............")
                speak("would you like to listen romantic music")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss.....................")
                    speak("boss you like this music")
                    music_dir = "D:\\music\\song"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[455]))

            #code for play album music
            elif'play album music'in query:
                speak("sure boss.................")
                speak("command is accepet..............")
                speak("would you like to listen album music")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss............................")
                    music_dir = "D:\\music\\listen\\ALBUM SONGS"
                    speak("enjoying to listening album music......")
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir,rd))

            #code for play Dj music
            elif'play Dj music'in query:
                speak("sure boss..............")
                speak("command is accepet...................")
                speak("would you like to listen Dj music")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss............")
                    music_dir = "D:\\music\\listen\\Dj"
                    speak("enjoying to listen dj music..............")
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir,rd))

            #code for play love music
            elif'play love music'in query:
                speak("sure boss..................")
                speak("command is accepet.....................")
                speak('would you like to listen ove music')
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss......................")
                    speak("i play love music....................")
                    music_dir = "D:\\music\\listen\\love song"
                    speak("enjoying to listen love music ")
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir,rd))

        #code for play movie
        elif'play movie'in query:
            speak("sure boss...................")
            speak("command is accept........................")
            speak("movie is opening ")
            movie_dir = "D:\\movie"
            movies = os.listdir(movie_dir)
            rd = random.choice(movies)
            os.startfile(os.path.join(movie_dir,rd))

        elif'play next movie'in query:
            speak("sure boss........................")
            speak("command is accepet..................")
            speak("next movie is playing")
            movie_dir = "D:\\movie"
            movies = os.listdir(movie_dir)
            rd = random.choice(movies)
            os.startfile(os.path.join(movie_dir, rd))

        #code for change movie
        elif'change movie'in query:
            speak("sure bos..............")
            speak("command is accept........")
            speak("movie is change")
            movie_dir = "D:\\movie"
            movies = os.listdir(movie_dir)
            rd = random.choice(movies)
            os.startfile(os.path.join(movie_dir, rd))

         #code for show photo
        elif'show photo'in query:
            speak("sure boss....................")
            speak("command is accept........")
            speak("photo is opening")
            photo_dir ="D:\\photo"
            photos = os.listdir(photo_dir)
            rd = random.choice(photos)
            os.startfile(os.path.join(photo_dir, rd))

        elif'next photo'in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("next photo is opening")
            photo_dir = " D:\\photo\\animation"
            photos = os.listdir(photo_dir)
            rd = random.choice(photos)
            os.startfile(os.path.join(photo_dir.rd))

        elif'change photo' in query:
            speak("sure boss....................")
            speak("command is accept........")
            speak("photo is change")
            photo_dir = "D:\\photo"
            photos = os.listdir(photo_dir)
            rd = random.choice(photos)
            os.startfile(os.path.join(photo_dir, rd))

        elif'show wallpaper'in query:
            speak("sure boss...................")
            speak("command is accept")
            speak("wallpaper is opening ")
            wallpaper_dir = "D:\\wallpaper"
            wallpapers = os.listdir(wallpaper_dir)
            rd = random.choice(wallpapers)
            os.startfile(os.path.join(wallpaper_dir,rd))

        elif'change wallpaper' in query:
            speak("sure boss")
            speak("command us accept")
            speak("wallpaper is change ")
            wallpaper_dir = "D:\\wallpaper"
            wallpapers = os.listdir(wallpaper_dir)
            rd = random.choice(wallpapers)
            os.startfile(os.path.join(wallpaper_dir, rd))

        elif'next wallpaper'in query:
            speak("sure boss..........")
            speak("command is accepet")
            wallpaper_dir = "D:\\wallpaper"
            wallpapers = os.listdir(wallpaper_dir)
            rd = random.choice(wallpapers)
            os.startfile(os.path.join(wallpaper_dir, rd))

         #code for open and close windows applications like c drive and d drive
        elif'open c drive'in query:
            speak("sure boss.................... ")
            speak("command is accepet................")
            speak("are you want to open a c drive")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss................")
                codepath = "C:"
                os.startfile(codepath)
                speak("boss c drive is opening ...........")

        ############# WORK ON COUNT FILE IN C DRIVE ##################
         #code for open program file and window file
        elif'open program files'in query:
            speak("sure boss..............")
            speak("command us accepet..............")
            speak("are you want to open programs files")
            replay  = takecommand()
            if'yes'in replay:
                speak("ok boss...................")
                codepath = "C:\\Program Files"
                os.startfile(codepath)
                speak("boss program file is opening......................")

        elif'open window section' in query:
            speak("sure boss................")
            speak("command is accepet......................")
            speak("are you want to open windows section")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...................")
                codepath = "C:\\Windows"
                os.startfile(codepath)
                speak("boss windows section is opening....................")

        elif'open d drive' in query:
            speak("sure boss.............")
            speak("command is accept............")
            speak("are you want to open d drive")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..............")
                codepath = "D:"
                os.startfile(codepath)
                speak("boss d drive is opening...........")

        elif'open photo section'in query:
            speak("sure boss..............")
            speak("command is accepet......")
            speak("are you want to open photo section")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...........")
                codepath = "D:\\photo"
                os.startfile(codepath)
                speak("boss photo section is opening ................")

        elif'open wallpaper section'in query:
            speak("sure boss..................")
            speak("command is accepet................")
            speak("are you want to open wallpaper section")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...........")
                codepath = "D:\\wallpaper"
                os.startfile(codepath)
                speak("boss wallpaper section is opening.............")

        elif'open music section'in query:
            speak("sure boss.........................")
            speak("command is accepet............................")
            speak("are you want to open music section..........")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..................")
                codepath = "D:\\music\\all music"
                os.startfile(codepath)
                speak("boss music section is opening............")

        elif'open movie section' in query:
            speak("sure boss.........................")
            speak("command is accepet............")
            speak("are you want to open movie section.........")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                codepath = "D:\\movie"
                os.startfile(codepath)
                speak("boss movie section is opening............")

        elif'open software section'in query:
            speak("sure boss............")
            speak("command is accept............")
            speak("are you want to open software section")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..................")
                codepath = "D:\\software"
                os.startfile(codepath)
                speak("boss software section is opening.................")

             ######################## CODE FOR WRITE A NOTE ####################
        elif'open note' in query:
            speak("sure boss...............")
            speak("command is accepet............")
            speak("are you want to show your note")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("showing note")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))

         #code for write a paragraph
        elif'write a paragraph'in query:
            speak("sure boss..................")
            speak("command is accepet...............")
            speak("are you want to write a paragraph..........")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("what should  i write in paragraph")
                note = takecommand()
                file = open('jarvis.txt', 'w')
                speak("boss i include date and time")
                snfm = takecommand()
                if 'yes' in snfm or 'sure' in snfm:
                    speak("ok i include date and time")
                    strtime = datetime.datetime.now().strftime("%H: %M: %S")
                    file.write(strtime)
                    file.write(":-")
                    file.write(note)
                else:
                    file.write(note)

        elif'open paragraph'in query:
            speak("sure boss.............")
            speak("command is accepet...............")
            speak("are you want to open and show paragraph")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("showing paragraph")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))

           #code for remember that or do you remember that6
        elif'remember that'in query:
            speak("sure boss..................")
            speak("command is accepet.............")
            speak("are you want  to ask me to remember something ")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.............")
                speak("tell me what should i remember,boss")
                remembermessage = takecommand()
                speak("you said me to remember"+remembermessage)
                remember = open('data.txt','w')
                remember.write(remembermessage)
                remember.close()

        elif'do you remember anything' in query:
            speak("sure boss..................")
            speak("boss wait a minute............")
            speak("let me check................")
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        # code for switch windows
        elif'switch window'in query:
            speak("sure boss...............")
            speak("command is accepet...........")
            speak("are you want to switch window")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("i automatically switching window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                speak("boss window is switch ")

            #code for shutdown pc and restart pc or sleep pc
            elif'shutdown the system'in query:
                speak("sure boss..................")
                speak("command is accepet.......................")
                speak("are you want to shutdown pc")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss..............")
                    speak("Make sure all the application are closed before shutdown the system")
                    speak("i automatically shutdown the system")
                    os.system("shutdown /s")
                    speak("boss all system is shutdown")
                elif'no'in replay:
                    speak("boss system is running...........")

            elif'restart the system'in query:
                speak("sure boss...............")
                speak("command is accepet...............")
                speak("are you want to restart pc")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok boss")
                    speak("make sure all the application are closed before restart the system")
                    speak("i automatically restart the system.............")
                    os.system("shutdown /r")
                    speak("all system are restart..........")
                elif'no' in replay:
                    speak("boss system is running...............")

            elif'log off the system'in query:
                speak("sure boss...............")
                speak("command is accepet.....................")
                speak("are you want to log off pc")
                replay = takecommand()
                if'yes'in replay:
                    speak("ok  boss..................")
                    speak("make sure all the application are closed before log off the system")
                    speak("i automatically log off the system.............")
                    subprocess.call(["shutdown", "/l"])
                    time.sleep(2)
                    speak("boss all system is log off")
                elif'no'in replay:
                    speak("boss system is not log off")

        #code for making advance virtual AI(the making a advance level virtual assistance to help me a login in some of website and switch thw windows and install some application in system)
        #code for chang your voice
        elif'change your voice'in query:
            speak("sure boss................")
            speak("command is accept.....................")
            speak("are you want to change my voice")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...........")
                speak("i switch my voices")
            if'female'in replay:
                 engine.setProperty('voice',voices[1].id)
            else:
                 engine.setProperty('voice',voices[0].id)
                 speak("boss i switch my voice")
                 speak("how it is ")

         #code for empty recycle bin
        elif'empty recycle bin'in query:
            speak("sure boss...................")
            speak("command is accepet...........................")
            speak("are you want to clean recycle bin")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.....................")
                speak(" i  automatically clean recycle bin")
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("recycle bin recycled")

        elif'lock window'in query:
            speak("sure boss...............")
            speak("command is accepet..............")
            speak("are you want to lock the system")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss.............")
                speak("i automatically lock all the system")
                speak("locking the all system.............")
                ctypes.windll.user32.LockWorkStation()

        elif'install turbo c'in query:
            speak("sure boss...................")
            speak("command is accepet...........")
            speak("are you want to install turbo c in system")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("i automatically install turbos c++ in system")
                time.sleep(1)
                speak("boss installation process is start ")
                fsv = Application(backend="win32").start( "D:\\software\\turbo c++ install\\Turbo C++ 4.0 Windows 7 Windows 8 64Bit Version.exe")
                fsv.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.IAgreeRadioButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.InstallButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.FinishButton.wait('ready', timeout=30).click_input()
                speak("boss turbo c software is installing successfully")

        elif'install notepad'in query:
            speak("sure boss........")
            speak("command is accepet.................")
            speak("are you want to install notepad in system")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("i automatically install notepad in system")
                time.sleep(1)
                speak("boss installation process is start ")
                fsv = Application(backend="win32").start("D:\\software\\npp install\\npp.7.8.Installer.x64.exe")
                fsv.InstallDialog.OkButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.IAgreeNextButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.InstallButton.wait('ready', timeout=30).click_input()
                fsv.InstallDialog.FinishButton.wait('ready', timeout=30).click_input()
                speak("boss notepad software is installing successfully ")

        #code for a send a message  in  whatsapp ,facebook and instagram or twitter
        #code for send a message in whatsapp
        elif'send a message'in query:
            speak("sure boss.................")
            speak("command is accepet...................")
            speak("are you want to send a message")
            replay = takecommand()
            if'yes'in replay:
                speak("what message i send boss")
                message = takecommand()
                speak("ok boss")
                speak("i send a message according to say.............")
                pywhatkit.sendwhatmsg("+91 9099770350",f"{message}",2,25)
                speak("message is send successfully")

        elif'send a message to father'in query:
            speak("sure boss...............")
            speak("command is accepet............")
            speak("are you want to send a message to your father")
            replay = takecommand()
            if'yes'in replay:
                speak("what message i send your father........")
                message = takecommand()
                speak("ok boss...............")
                speak("i send a message to your father according to say")
                pywhatkit.sendwhatmsg("+91 9099770350",f"{message}",2,25)
                speak("message is send to your father successfully")

        elif'send a message to uncle' in query:
            speak("sure boss...............")
            speak("command is accepet....................")
            speak("are you want to send a message to your uncle")
            replay = takecommand()
            if'yes'in replay:
                speak("what message i send your uncle")
                message = takecommand()
                speak("ok boss.................")
                speak("i send a message to your uncle according to say ")
                pywhatkit.sendwhatmsg("+09427502556",f"{message}",2,25)
                speak("message is send to your uncle is successfully")

        elif'send a message to khushi' in query:
            speak("sure boss..........................")
            speak("command is accepet......................")
            speak("are you want to send a message to khushi")
            replay = takecommand()
            if'yes'in replay:
                speak("what message i send to your sister")
                message = takecommand()
                speak("ok boss......................")
                speak("i send a message to your sister according to say")
                pywhatkit.sendwhatmsg("+91 6354877342",f"{message}",2,25)
                speak("boss message is successfully send to your sister khushi")

          #code for sand a message in whatsapp group
        elif'send a message to whatsapp group'in query:
            speak("sure boss..................................")
            speak("command is accepet..........................")
            speak("are you want to send a message to whatsapp group")
            replay = takecommand()
            if'yes'in replay:
                speak("what message i send to whatsapp group ")
                message = takecommand()
                speak("ok boss..................")
                speak("i send a message to whatsapp group according to say")
                pywhatkit.sendwhatmsg_to_group("sweet family",f"{message}",2,25)
                speak("boss message is successfully send to whatsapp group")

           ####################### CODE FOR VOLUME UP ######################
        elif'volume up'in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("are you want to volume up")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("i automatically volume up ")
                pyautogui.press("volumeup")
                speak("boss volume is up")

           ####################### CODE FOR VOLUME DOWN ###################
        elif'volume down' in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("are you want to volume up")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss")
                speak("i automatically volume up ")
                pyautogui.press("volumedown")
                speak("volume is down")

        #################### CODE FOR VOLUME MUTE ############################
        elif'volume mute'in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("are you want to volume up")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss")
                speak("i automatically volume up ")
                pyautogui.press("volumemute")
                speak("volume is mute")

        ######################## CODE FOR TELLING JOKES ##########################33
        #code for telling jokes
        elif'tell me jokes'in query:
            speak("sure boss..................")
            speak("command is accepet....................")
            speak("are you want to listen the jokes")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...................")
                speak("i automatically tell you jokes")
                speak("here you can listen a funny jokes")
                speak("enjoying to listen funny jokes")
                list_of_jokes = pyjokes.get_jokes(language="en",category="neutral")
                for i in range(0,90):
                    print(list_of_jokes[i])
                    speak(list_of_jokes[i])

           #work on screenshot
         #code for take screenshot
        elif'screenshot'in query:
            speak("sure boss..............................")
            speak("command is accepet.................................")
            speak("are you want to take a screenshot")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss...............")
                speak("wait a minute ...............")
                speak("i automatically take a screenshot.................")
                myscreenshot = pyautogui.screenshot()
                myscreenshot.save("D:\\python work\\screenshot\\filename1.png")
                speak("successfully  take a screenshot")
                speak("here you can see screenshot")
                codepath = "D:\\python work\\screenshot\\filename1.png"
                os.startfile(codepath)

        #code for read a pdf and read a ppt
        #code for read a pdf
        elif'read a pdf'in query:
            speak("sure boss....................")
            speak("command is accepet........................")
            speak("are you want to read a pdf............")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.................")
                speak("i automatically read the pdf")
                book = open('Chapter-2-Analysis of Algorithms.pdf', 'rb')
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.numPages
                speak(f"total numbers of pages in this book is{pages}")
                speak("boss please enter the page number i have to read")
                pg = int(input("please enter the page number"))
                page = pdfReader.getPage(pg)
                text = page.extractText()
                speak(text)


        ################# CODE FOR SIMPLE QUESTION AND ANSWER ###############################
        #code for given simple question and answer
        elif'how are you'in query:
            speak("i am fine sir")
            speak("how are you")

        elif'i am fine' in query:
            speak("ok boss")
            speak("this is good for your health")

        elif'reason for you' in query:
            speak("i am major project of mister sumit parmar")
            speak("i am build  because i perform every task or oder which given by my boss  ")
            speak("i perform every task ")

        elif'do you believe in god'in query:
            speak("i always believed in god")


                         ################## WOK IN GOOGLE MAP#################
        ############################### CODE FOR HIGH LEVEL ADVANCE ###########################
        ############################## CODE FOR CHECK CPU DATA ###################################a
        elif'show CPU DATA'in query:
            speak("sure boss")
            speak("command is accepet...............")
            speak("are you want to show CPU data in your system........")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.................")
                speak("i automatically open task manager and you can see cpu data")
                speak("wait a minute")
                speak("task manager is opening.............")
                os.system("task manager")
                speak("here you can see all cpu data in your system")

        ########################## CODE FOR CHECK RUNNING PROCESS##################
        elif'check running process' in query:
            speak("sure boss................")
            speak("command is accepet.........................")
            speak("are you want to check running process...................")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss,i automatically check the running process")
                speak("wait a minute boss")
                f = wmi.WMI()
                speak("pid  process name")
                print("pid  process name")
                for process in f.Win32_Process():
                     print(f"{process.ProcessId:<10} {process.Name}")
                     speak(f"{process.ProcessId:<10} {process.Name}")
                speak("here you can see running process in system............."

        ############################### CODE FOR ADJUST BRIGHTNESS######################
        elif'adjust brightness' in query:
            speak("sure boss")
            speak("command is accepet...............")
            speak("are you want to set screen  brightness")
            replay = takecommand()
            if'yes'in replay:
                speak("ok ,tell me which value i set the screen brightness")
                value = takecommand()
                if'15'in value:
                    speak("sure boss")
                    speak("i automatically set brightness at 15 percentage")
                    os.system("start ms-settings:display")
                    time.sleep(1)
                    sbc.set_brightness(15)
                elif'75'in value:
                    speak("sure boss")
                    speak("i automatically set brightness at 75 percentage ")
                    os.system("start ms-settings:display")
                    time.sleep(1)
                    sbc.set_brightness(75)
                elif'55'in value:
                    speak("sure boss ")
                    speak("i automatically set brightness at 55 percentage ")
                    os.system("start ms-settings:display")
                    time.sleep(1)
                    sbc.set_brightness(55)
                elif'25'in value:
                    speak("sure boss")
                    speak("i automatically set brightness at 25 percentage")
                    os.system("start ms-settings:display")
                    time.sleep(1)
                    sbc.set_brightness(25)
                elif'95'in value:
                    speak("sure boss")
                    speak('i automatically set brightness at 95 percentage ')
                    os.system("start ms-settings:display")
                    sbc.set_brightness(95)
                    os.system("start ms-settings:display")

                ################# CODE FOR LOGIN IN GMAIL ACCOUNT ###################

                ###############33 CODE FOR CHANGING BACK GROUND WALLPAPER #######################
        #code for change back ground wallpaper
        elif'change background wallpaper'in query:
            speak("sure boss......................")
            speak("command is accepet............................")
            speak("are you want to change back ground wallpaper..................")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss..................")
                speak("i automatically change back ground wallpaper..................")
                img = "D:\\wallpaper"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak("back ground wallpaper is changed")

        #code for check current temp
        elif'current temperature'in query:
            speak("sure boss........................")
            speak("command is accepet.......................")
            speak("are you want to check current temperature ")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss........................")
                speak("wait a minute .......................")
                speak("i automatically check the current temperature ")
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                CITY = "junagadh"
                API_KEY = "98bb246f4a4889ec93b07854e388e1d7"
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    temperature = main['temp']
                    humidity = main['humidity']
                    pressure = main['pressure']
                    report = data['weather']
                    speak(f" the Temperature of junagadh city is: {temperature}")
                    speak(f" the Humidity of junagadh city : {humidity}")
                    speak(f"Pressure: {pressure}")
                    speak(f"the Weather Report of junagadh city is : {report[0]['description']}")
                else:
                    print("Error in the HTTP request")

           #code for check current whether
        elif'current weather'in query:
            speak("sure boss.......................")
            speak("command is accepet.........................")
            speak("are you want to check current weather.....................")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss.....................")
                speak("wait a minute.....................")
                speak("i automatically check the current whether  ")
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                CITY = "junagadh"
                API_KEY = "98bb246f4a4889ec93b07854e388e1d7"
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    report = data['weather']
                print(f"the current weather is : {report[0]['description']}")
                speak(f"the current weather is : {report[0]['description']}")

        ################################### CODE FOR CHECK INTERNET SPEED #######################3
        #code for check internet speeds
        elif'check internet speed'in query:
            speak("sure boss")
            speak("command is accepet...................")
            speak("are you want to check internet speed")
            replay = takecommand()
            if'yes'in replay:
                speak("ok boss")
                speak("i automatically checking internet speed")
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                print(f"boss we have{dl}bit per second downloading speed and {up}bit per second uploading speed")
                speak(f"boss we have{dl}bit per second downloading speed and {up}bit per second uploading speed")

        #code for searching and knowing anything
        elif'activated how to do mode' in query:
            speak("sure boss.............")
            speak("command is accepet.............")
            speak("are you want to active activated how to do mode")
            replay = takecommand()
            if 'yes' in replay:
                speak("ok boss..............")
                speak("how to do mod is activated please tell me what you want to know")
                how = takecommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

        #code for check system battery
        elif'battery'in query:
            speak("sure boss..............")
            speak("command is accepet................")
            speak("are you want to check system battery...........")
            replay  = takecommand()
            if'yes'in replay:
                speak("ok boss.................")
                speak("i check system battery")
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"boss system have{percentage} percent battery")
                if percentage >= 75:
                     speak(" boss,we have enough power to continue our work")
                elif percentage >= 40 and percentage <= 75:
                     speak("boss,we should connect our system to charging point to charge our battery")
                elif percentage <= 15 and percentage <= 30:
                     speak("boss,we don't have enough power to work,pleas connect to charging ")
                elif percentage <= 15:
                     speak("boss,we have very low power ,please connect to charging the system well shutdown very soon")

        elif'sleep' in query:
            speak("sure boss")
            speak("command is accepet..............")
            speak("i am going to sleep now")
            sys.exit()







