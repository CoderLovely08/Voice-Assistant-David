# importing all the required modules
import os
import platform
import webbrowser
from time import sleep
from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import cv2
import psutil
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import pywhatkit as kit
import requests
import screen_brightness_control as sbc
import speech_recognition as sr
import speedtest
import wikipedia
import wolframalpha
from bs4 import BeautifulSoup
from covid import *
from keyboard import *
from PIL import Image, ImageTk
from pyautogui import *
from requests import get

from generalResponse import responseDictionary

# initialising speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

queryLogger = []
queryIndex = -1

window = Tk()
window.geometry('800x800')
window.minsize(1200, 800)
window.maxsize(1200, 800)

var = StringVar()
var1 = StringVar()

labelImage = Image.open('images/labelBackground.jpg')
resizedLabelImage = labelImage.resize((200, 50), Image.LANCZOS)
updatedLabelImage = ImageTk.PhotoImage(resizedLabelImage)

startButtonImage = Image.open('images/Start.png')
resizedStartImage = startButtonImage.resize((125, 40), Image.LANCZOS)
updatedStartButtonImage = ImageTk.PhotoImage(resizedStartImage)

ExitButtonImage = Image.open('images/Quit.png')
resizedExitImage = ExitButtonImage.resize((125, 40), Image.LANCZOS)
updatedExitButtonImage = ImageTk.PhotoImage(resizedExitImage)

backgroundImage = Image.open('images/back1.png')
resizedBackgroundImage = backgroundImage.resize((1200, 800), Image.LANCZOS)
updatedBackgroundImage = ImageTk.PhotoImage(resizedBackgroundImage)

fileObj = open("QueryLog.txt", 'a')
strTime = datetime.datetime.now().strftime("%H:%M:%S")
fileObj.write(strTime)

# speak function for text to speech output
def speak(audio):
    engine.say(audio)
    var.set(audio)
    window.update()
    print(audio)
    fileObj = open("QueryLog.txt", 'a')
    writeQueryLog = '\n'+audio
    fileObj.write(str(writeQueryLog))
    engine.runAndWait()

query = ''

# this allows the program to take user input in the form of audio //speech recognition functionality
# noinspection PyBroadException
def takecommand():
    global query, queryIndex, queryLogger

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        var1.set('listening...')
        window.update()
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print('recognising...')
        var1.set('recognising...')
        window.update()
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
        var1.set(query)
        window.update()
        fileObj = open("QueryLog.txt", 'a')
        queryLogText = '\n' + query
        fileObj.write(str(queryLogText))

    except Exception:
        query = ''
    return query.lower()

# initialising system
def initialiseSystem():
    try:
        speak("Initialising system. Hello, i am David, your Personal Voice Assistant,"
              " from now i will be your companion in most of the tasks, and i will assist you as best as i can.")
        ramUsage = psutil.virtual_memory()[2]
        cpuUsage = psutil.cpu_percent(2)
        batteryCheck = psutil.sensors_battery()
        try:
            percentage = batteryCheck.percent
        except:
            percentage = "Plugged power source"

        speak(f"Your current battery level is at {percentage} %")
        speak(f'RAM memory {ramUsage} % used:')
        speak(f'The CPU usage is: {cpuUsage} %')
        speak("All systems are fully operational.")
        speak("Now tell me, what can i do for you?")
    except:
        speak("Some error has occurred, wait for a moment i am fixing it")

# greets the user along with time
def wish():
    try:
        hour = int(datetime.datetime.now().hour)
        tt = time.strftime("%I:%M %p")

        if hour in range(0, 13):
            speak(f'Good Morning, its {tt}')
        elif hour in range(12, 18):
            speak(f'Good Afternoon, its {tt}')
        else:
            speak(f'Good Evening, its {tt}')
    except:
        speak("Some error has occurred")

# key board shortcut function
def keyboardShortcut(shortcutQuery):
    try:
        file = open('File.txt', 'r')
        value = ''
        counter = 0
        keyResults = shortcutQuery.lower()
        keyResults = keyResults.split()
        if 'of' in keyResults:
            searchIndex = keyResults.index('of')
            value = keyResults[searchIndex + 1]
            value = value.capitalize()
        if 'for' in keyResults:
            searchIndex = keyResults.index('for')
            value = keyResults[searchIndex + 1]
            value = value.capitalize()
        for line in file:
            if value in line:
                counter += 1
                speak(line)
                if counter == 3:
                    break
        if counter == 0:
            speak("Sorry i couldn't find any relevant solution for this")
        else:
            speak(f' i found {counter} solutions ')
    except:
        speak("It seems like, some system files are missing please check all program related files.")

# opens google chrome with google as home page
def launchGoogle():
    try:
        speak("sir, what should i search on google")
        searchQuery = takecommand().lower()
        if "i will" in searchQuery or "not" in searchQuery or "don't" in searchQuery:
            webbrowser.open("https://www.google.com")
        else:
            webbrowser.open("https://www.google.com/search?q=" + searchQuery)
    except:
        speak("Something went wrong while performing search")

def preprocess_email(email):
    # Reverse the email address and replace the first occurrence of "ta" with "@"
    processed_email = email[::-1].replace("ta", "@", 1)[::-1].replace(" ", "")
    
    return processed_email.lower()

def send_email():
    try:
        # Sender's email is already stored
        sender_email = "davidvoiceassistant7@gmail.com"
        password = "kvpe bluh srlf xxcb"
        
        # Speak and listen for recipient email
        speak("Who would you like to send the email to?")
        receiver_email = takecommand().lower()
        receiver_email = preprocess_email(receiver_email)
        speak(f"Sending email to {receiver_email}")

        # Confirm recipient email
        confirm = ""
        while "yes" not in confirm:
            speak("Say yes to confirm the recipient email address")
            confirm = takecommand().lower()
            if "yes" not in confirm:
                speak("Please say yes to confirm or provide the email again.")
                receiver_email = takecommand().lower()
                receiver_email = preprocess_email(receiver_email)
                speak(f"Sending email to {receiver_email}")
            if "cancel" in confirm:
                speak("Email sending cancelled")
                return

        # Speak and listen for subject
        speak("What should be the subject of the email?")
        subject = takecommand().lower()
        
        # Speak and listen for body
        speak("What message would you like to send?")
        body = takecommand().lower()
        
        # Inform user that email is being sent
        speak("Sending email in the background. Please wait.")
        
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # Email body
        message.attach(MIMEText(body, 'plain'))

        # SMTP server setup for Gmail
        smtp_server = "smtp.gmail.com"
        port = 587  # Gmail SMTP port

        # Start TLS connection
        context = smtplib.SMTP(smtp_server, port)
        context.starttls()

        # Login to Gmail
        context.login(sender_email, password)

        # Send email
        text = message.as_string()
        context.sendmail(sender_email, receiver_email, text)

        # Close connection
        context.quit()
        
        speak("Email sent successfully!")
    except Exception as e:
        print(e)
        speak("Something went wrong while sending the email")

# this function returns currently active cases in india
def covidCases():
    try:
        currentCases = Covid()
        speak("Which country data you are looking for")
        countryName = takecommand().capitalize()
        case = currentCases.get_status_by_country_name(countryName)
        country = case['country']
        active = case['active']
        deaths = case['deaths']
        recovered = case['recovered']
        speak(f"Country is {country}\n"
              f"Currently active cases are {active}\n"
              f"Total recovered cases are {recovered}\n"
              f"Total deaths till now are {deaths}\n")
    except:
        speak("that doesn't seem to be a country name, please try again")
        covidCases()

# whatsapp automation
def whatsappAutomation(name, message):
    speak('Opening whatsapp')
    os.startfile('C:\\Users\\LENOVO\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    sleep(8)
    click(325, 142)  # search contact
    sleep(3)
    write(name)  # search name
    sleep(3)
    click(305, 295)  # click on search result
    sleep(3)
    click(990, 990)  # click on message input field
    sleep(3)
    write(message)   # write message in enter message field
    sleep(1)
    press('enter')  # hit enter
    speak(f'Your message has been sent successfully to {name}')

# whatsapp voice call
def whatsappCall(calltype, name):
    speak('Opening whatsapp')
    os.startfile('C:\\Users\\LENOVO\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    sleep(8)
    click(325, 142)  # search contact
    sleep(2)
    write(name)  # search name
    sleep(3)
    click(305, 295)  # click on search result
    sleep(3)
    if calltype == 'voice':
        click(1724, 73)  # click on call button
    elif calltype == 'video':
        click(1661, 73)  # click on video call button
    speak(f"Calling, {name}")

# creating meeting link
def createMeetLink():
    speak("Opening google meet to start an instant meeting")
    webbrowser.open("https://meet.google.com/")
    sleep(5)
    click(205, 712)
    sleep(5)
    click(285, 768)
    speak("Your meeting has started, now you can ask others to join your meeting")

# joining pwp class
def joinClass(code):
    speak("Opening google meet to join class")
    webbrowser.open("https://meet.google.com/")
    sleep(10)
    click(510, 720)     # entering the class code
    sleep(2)
    write(code)     # paste class code
    sleep(2)
    click(643, 717)     # click on join
    sleep(10)
    click(1305, 638)    # click on ask to join
    speak("Wait until someone lets you in")

# changing system volume as per user convenience
def changeVolume(string):
    try:
        getString = ''
        if 'change' in string:
            speak("by how much % should i increase or decrease the volume?")
            getString = takecommand()
            getValue = getIntegers(getString)
        else:
            getValue = getIntegers(string)
        taps = int(getValue / 10) * 5
        if 'up' in string or "increase" in string or 'up' in getString or "increase" in getString:
            for i in range(taps):
                pyautogui.press('volumeup')
            speak(f"Volume level increased by {getValue}%")
        elif 'down' in string or 'decrease' in string or "lower" in string or 'down' in getString or 'decrease' in getString or "lower" in getString:
            for i in range(taps):
                pyautogui.press('volumedown')
            speak(f"Volume level decreased by {getValue}%")

    except:
        speak("Something went wrong, while changing system volume")

# news function
def NewsFromBBC():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        speak(results[i])

# returns integers only in a given string
def getIntegers(string):
    try:
        if '%' in string:
            string = string.replace('%', '')
        if '°C' in string:
            string = string.replace('°C', '')
        numbers = [int(word) for word in string.split() if word.isnumeric()]
        return numbers[0]
    except:
        return []

# increases and decreases brightness as per user command
def brightnessControl(changeBrightnessCommand):
    try:
        brightnessLevel = getIntegers(changeBrightnessCommand)

        getCurrentBrightness = sbc.get_brightness()
        if "increase" in changeBrightnessCommand:
            sbc.set_brightness(getCurrentBrightness + brightnessLevel)
            speak(f"Brightness increased by {brightnessLevel}%")

        else:
            sbc.set_brightness(getCurrentBrightness - brightnessLevel)
            speak(f"Brightness decreased by {brightnessLevel}%")
    except:
        speak("something went wrong while changing brightness level")

# this function returns day of week
def getDay():
    day = datetime.datetime.today().weekday()+1
    print(day)
    dayDict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    if day in dayDict.keys():
        speak(f"it's {dayDict[day]} today")

# to check for internet speed
def getInternetSpeed():
    speak("Checking for your internet speed, this might take a while")
    speed = speedtest.Speedtest()
    upload = round(speed.upload() / 10 ** 6, 2)
    download = round(speed.download() / 10 ** 6, 2)
    speak(f"Your upload speed is {upload} MBPS \nYour download speed is {download} MBPS ")
    if upload < 5.0:
        speak("Your upload speed is slow")
    if download < 10:
        speak("Your download speed is slow")
    if download in range(10, 16):
        speak("Your download speed is average")
    if download > 20:
        speak("Your download speed is perfectly fine")

# system information function
def systemInformation():
    my_system = platform.uname()
    speak(f"Your system is {my_system.system}\n"
          f"Node name is {my_system.node}\n"
          f"Release {my_system.release}\n"
          f"Version {my_system.version}\n"
          f"Machine {my_system.machine}\n"
          f"Processor {my_system.processor}")

# Function to send request to the language model API
def send_request(text):
    LANGUAGE_MODEL_API_KEY = 'AIzaSyDTLs2INVs8tWklZ4eRg_Gb-u27-TS9tCw'
    LANGUAGE_MODEL_URL = f'https://generativelanguage.googleapis.com/v1beta1/models/chat-bison-001:generateMessage?key={LANGUAGE_MODEL_API_KEY}'
    payload = {
        'prompt': {'messages': [{'content': text}]},
        'temperature': 0.1,
        'candidate_count': 1,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(LANGUAGE_MODEL_URL, json=payload, headers=headers)
    return response.json()['candidates'][0]['content']


# main function in which main logic of code resides
def runAssistant():
    global query, queryLogger
    wish()
    # initialiseSystem()
    while True:
        query = takecommand()
        fileObj = open("QueryLog.txt", 'a')
        fileObj.write(str(queryLogger))
        
        if "notepad" in query or 'editor' in query:
            if "open" in query:
                speak("Opening Notepad")
                os.startfile("C:\\Windows\\System32\\notepad.exe")
            elif "close" in query:
                speak("Notepad closed")
                os.system("taskkill /f /im notepad.exe")
            continue

        # for command prompt
        elif "command prompt" in query or 'cmd' in query or 'terminal' in query:
            if "open" in query:
                speak("Opening Command prompt ")
                os.system("start cmd")
            elif "close" in query:
                speak("Command prompt terminated")
                os.system("taskkill /f /im cmd.exe")
            continue

        #  to open camera
        elif "open camera" in query:
            speak("Opening Camera, get ready")
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(10)
            if k == 27:
                cap.release()
                cv2.destroyAllWindows()
            continue

        # play music
        elif "music" in query or "song" in query:
            speak("sir, what song should i play")
            searchQuery = takecommand().lower()
            if 'play' in searchQuery:
                searchQuery = searchQuery.replace('play', '')
            kit.playonyt(searchQuery)
            speak("your song is being played on youtube")
            speak("Sir i am still here in case you need me.")
            continue

        # for ip address
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")
            continue

        # wikipedia
        elif "wikipedia" in query:
            try:
                speak("What should i search on wikipedia")
                cm = takecommand()
                webbrowser.open("https://en.m.wikipedia.org/wiki/" + cm)
                results = wikipedia.summary(cm, 2)
                speak("according to wikipedia" + results)
            except:
                speak("Some error has occurred, try something else")
            continue

        # opening youtube in default browser
        elif "youtube" in query and "open" in query:
            try:
                speak('What should i search on youtube?')
                searchQuery = takecommand()
                if "i will" in searchQuery or "nothing" in searchQuery or "don't search" in searchQuery:
                    speak("Alright sir, opening youtube")
                    webbrowser.open("www.youtube.com")
                elif 'search for' in searchQuery:
                    searchQuery = searchQuery.replace('search for', '')
                    speak(f"Alright sir, searching for {searchQuery} on youtube")
                    webbrowser.open("https://www.youtube.com/search?q=" + searchQuery)
                    time.sleep(5)
                    speak("here are your results. Sir i am still here in case you need me.")
                else:
                    speak(f"Alright sir, searching for {searchQuery} on youtube")
                    webbrowser.open("https://www.youtube.com/search?q=" + searchQuery)
                    time.sleep(5)
                    speak("here are your results. Sir i am still here in case you need me.")
            except:
                speak("Some error has occurred, try something else")
            continue

        # closing youtube
        elif "close" in query and "youtube" in query:
            press_and_release("ctrl+w")
            speak('Closing Youtube')
            continue

        # opening facebook in chrome
        elif "facebook" in query:
            if "open" in query or "start" in query or 'check' in query:
                speak("Opening your facebook account")
                webbrowser.open("www.facebook.com")
            elif 'close' in query:
                speak("Done, facebook closed")
                press_and_release("ctrl + w")
            speak("Alright sir, i am still here in case you need me.")
            continue

        # opening default browser //chrome
        elif "chrome" in query:
            if "open" in query:
                launchGoogle()
            elif "close" in query or 'terminate' in query:
                os.system("taskkill /im chrome.exe /f")
                speak("Chrome terminated")
            continue

        # to find joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            continue

        # google search using web scraping
        # this reads the top article and also redirects the user to the browser
        elif "google" in query or "search" in query or "tell me about" in query:
            import wikipedia as googleScrap
            if "google" in query:
                query = query.replace('google', "")
            if "search" in query:
                query = query.replace("search", '')
            elif 'tell me about' in query:
                query = query.replace("tell me about", '')
            else:
                query = query.replace("tell me", '')
            speak("this is what i have found on web")
            pywhatkit.search(query)
            try:
                searchResult = googleScrap.summary(query, 2)
                speak(searchResult)
            except:
                speak("sorry but no data available for your search")
            finally:
                speak("Now you can continue")
            continue

        # switch current window
        elif "switch" in query:
            if "tab" in query or "window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                speak("Tab switched")
            continue

        # takes screenshot of the current screen within 1 second
        elif "screenshot" in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\LENOVO\Pictures\Screenshots\screenshot1.png')
            speak("Screenshot captured")
            continue

        # tells us the temperature of particular location
        elif "temperature" in query:
            try:
                query = query.split()
                ind = query.index('in') + 1
                search = "temperature in " + query[ind]
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                try:
                    if int(getIntegers(temp)):
                        speak(f"current {search} is {temp}")
                except:
                    speak("City not found, please check the city name and try again")
            except:
                    speak("City not found, please check the city name and try again")
            continue

        # helps in finding keyboard shortcuts
        elif 'shortcut' in query:
            keyboardShortcut(query)
            continue

        # appreciating assistant
        elif "good job" in query or "well done" in query or "thank" in query or "great job" in query or 'nice' in query:
            speak("That's so nice to hear from you. I am still here in case you need me")
            continue

        # to find deals and for online shopping
        elif "deal" in query or "shop" in query or "amazon" in query:
            speak("okay, let me open an online shopping site")
            speak("i can open amazon, so i am opening amazon")
            webbrowser.open("https://www.amazon.com/")
            continue

        # opens instagram on user command
        elif "instagram" in query:
            if "open" in query or "start" in query:
                speak("okay, let me open your insta account")
                time.sleep(0.5)
                webbrowser.open("https://www.instagram.com")
            elif 'close' in query:
                press_and_release("ctrl + w")
                speak("Done, instagram closed")
            else:
                speak("Sir, i am still here in case you need me.")
            continue

        # Email sending
        if 'email' in query:
            send_email()
            continue
        
        # texting on whatsapp
        elif 'message' in query or 'text' in query:
            #if 'whatsapp' in query:
            speak('to whom do you wanna text')
            getContactName = takecommand()
            speak(f'Tell me what message you want to send to {getContactName}')
            getUserMessage = takecommand()
            whatsappAutomation(getContactName, getUserMessage)
            speak("Sir, i am still here in case you need me.")
            continue

        # calling on whatsapp
        elif 'call' in query:
            speak("To whom do you wanna call")
            getContactName = takecommand()
            if 'video' in query:
                whatsappCall('video', getContactName)
            else:
                whatsappCall('voice', getContactName)
            continue

        # creating meeting link
        elif 'create meet' in query or 'meet' in query or 'create link' in query:
            createMeetLink()
            continue

        elif 'join' in query:
           if 'pwp' in query or "python" in query:
               meetingCode = 'uwz-ckdt-aut'
               joinClass(meetingCode)
           continue

        # repeats user query
        elif "repeat" in query or 'respond' in query:
            if "after me" in query or "my word" in query or "what i say" in query:
                speak("Sure sir, go ahead")
                jj = takecommand()
                speak(f"you said :{jj}")
            continue

        # for saving user notes
        elif "note" in query:
            if "take" in query or "write" in query or 'save' in query:
                speak("What should i write in the note, sir")
                note = takecommand()
                speak("Please select a file name")
                fileName = takecommand()
                file = open(f'{fileName}.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takecommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak(f"file saved as {fileName}")
                else:
                    file.write(note)
                    speak(f"file saved as {fileName}")
            if 'show' in query:
                try:
                    speak("Showing Notes")
                    file = open(f"{fileName}.txt", "r")
                    speak(file.read())
                except:
                    speak("Sorry, but it looks like you don't have any saved notes yet")
            continue

        # to return latest news headlines
        elif "news" in query or 'headline' in query:
            NewsFromBBC()
            continue

        # tells us system information
        elif "system" in query or "tell me about my system" in query:
            if "info" in query or "about" in query or "status" in query or 'configuration' in query:
                systemInformation()
            continue

        elif "volume" in query:
            changeVolume(query)
            continue

        # opens word
        elif "word" in query:
            if "open" in query or 'start' in query:
                speak("Opening Microsoft word")
                os.startfile("Winword.exe")
            elif 'close' in query:
                speak("Microsoft Word terminated")
                os.system("taskkill /f /im Winword.exe")
            continue

        # opens excel
        elif "excel" in query:
            if "open" in query or 'start' in query:
                speak("Opening Microsoft excel")
                os.startfile("Excel.exe")
            elif 'close' in query:
                speak("Microsoft Excel terminated")
                os.system("taskkill /f /im Excel.exe")
            continue

        # opens powerpoint
        elif "power point" in query or "powerpoint" in query or "presentation" in query:
            if "open" in query or 'start' in query:
                speak("Opening Microsoft Power Point")
                os.startfile("Powerpnt.exe")
            elif 'close' in query:
                speak("Microsoft Power Point terminated")
                os.system("taskkill /f /im Powerpnt.exe")
            continue

        elif 'which day' in query:
            getDay()
            continue

        # enables sleep mode for specified time limit
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want me to stop listening for commands")
            getSleepTime = takecommand()
            if 'minute' in getSleepTime:
                varTimeforSleep = getIntegers(getSleepTime)*60
                if varTimeforSleep == 60:
                    speak(f"sleep mode initiated for 1 minute")
                    time.sleep(varTimeforSleep)
                else:
                    speak(f"sleep mode initiated for {getIntegers(getSleepTime)} minutes")
                    time.sleep(varTimeforSleep)
            elif 'second' in getSleepTime:
                varTimeforSleep = getIntegers(getSleepTime)
                speak(f"sleep mode initiated for {varTimeforSleep} seconds")
                time.sleep(varTimeforSleep)
            elif 'hour' in query:
                speak("sorry, but i cannot stay active in background for that much long time")
            else:
                speak(f"sleep mode initiated for default 1 minute")
                time.sleep(60)
            continue

        # downloads youtube video
        elif "download" and "youtube" in query:
            speak("Sir please provide the video link and select the destination in order to download the video")
            os.system("python YoutubeDownloader.py")
            speak("Your Video is downloaded")
            continue

        # tells us covid cases in a particular country
        elif "covid" in query or "corona" in query or 'pandemic status' in query or 'pandemic situation' in query:
            covidCases()
            continue

        # to open pycharm
        elif 'code' in query or 'update' in query or 'project' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\pycharm64.exe")
            speak("Alright sir, opening py charm for you.")
            sleep(2)
            speak("This might take a while")
            continue

        elif "do nothing" in query:
            speak("Alright sir, i am still here in case you need me")
            continue

        elif 'initiate' in query or 'initialise' in query or 'reboot' in query:
            initialiseSystem()
            continue

        # this part reminds user his/her message
        elif "remember" in query:
            remember = open("remember.txt", "w")
            if 'remember that' in query:
                rememberMsg = query.replace("remember that", "")
                speak("you asked me to remind you that :" + rememberMsg)
                remember.write(rememberMsg)
            elif 'do you remember' in query:
                rememberFile = open("remember.txt", "r")
                speak("you asked me that" + rememberFile.read())
            else:
                speak("What do you want me to remember?")
                rememberText = takecommand()
                if 'remember that' in rememberText:
                    rememberMsg = rememberText.replace("remember that", "")
                    speak("you asked me to remember that :" + rememberMsg)
                    remember.write(rememberMsg)
                else:
                    speak("you asked me to remember that :" + rememberText)
                    remember.write(rememberText)
            remember.close()
            continue

        elif 'bore' in query or 'game' in query or 'play' in query:
            if 'bore' in query:
                speak("in that case, i can help to get rid of boredom. Do you wanna play tic tac toe? or you want to listen a joke")
                gameName = takecommand()
                if 'game' in gameName or "tic" in gameName or 'play' in gameName:
                    speak('Alright, get ready to play tic tac toe')
                    os.system('python Game.py')
                if 'joke' in gameName:
                    joke = pyjokes.get_joke()
                    speak(joke)
            elif 'game' in query or 'play' in query:
                speak('Alright, get ready to play tic tac toe')
                os.system('python Game.py')
            continue

        # changing brightness level
        elif 'bright' in query:
            brightnessControl(query)
            continue

        elif 'to sleep' in query:
            speak("yeah, i also feel that i should take a nap, let me have a quick power nap of 5 minutes.")
            sleep(300)
            continue

        # to check internet speed
        elif 'speed' in query or 'connection' in query or "internet" in query:
            getInternetSpeed()

        # for waiting for a certain amount of time
        elif 'wait' in query or 'hold' in query:
            varTimeforSleep = getIntegers(query)     # this will return a list of numbers in query
            if 'minute' in query:
                varTimeforSleep *= 60
                if varTimeforSleep == 60:
                    speak(f"waiting for 1 minute till the next command")
                    sleep(varTimeforSleep)
                else:
                    speak(f"waiting for {getIntegers(query)} minutes till the next command")
                    time.sleep(varTimeforSleep)
            elif 'second' in query:
                speak(f"waiting for {varTimeforSleep} seconds till the next command")
                time.sleep(varTimeforSleep)
            speak("Tell me sir, what you want me to do now?")
            continue

        #for responding to general questions
        elif query in responseDictionary.keys():
            user = query
            dictVar = responseDictionary
            if user in dictVar.keys():
                speak(dictVar[user])
            continue

        elif "rest" in query or 'bye' in query or 'close project' in query or "shut" in query:
            if "shut" in query:
                speak("okay sir. Terminating all programs make sure you have saved all your files.")
            else:
                speak("Okay Sir, you can call me anytime. Now let me have some rest.")
            sys.exit()

        # final block for wolframalpha
        else:
            try:
                question = query
                speak(send_request(question))
            except:
                speak("can you please say that again")
            continue


def exitAssistant():
    sys.exit()

# Call main function
if __name__ == "__main__":
    bglabel = Label(window, image=updatedBackgroundImage)
    bglabel.place(x=0, y=0)

    label2 = Message(window, textvariable=var1, width=450, fg='#0f0', bg='#000', font=('Courier', 10))
    var1.set('User Said:')
    label2.place(x=75, y=75)

    label1 = Message(window, textvariable=var, width=450, fg='#00ff00', bg='#000', font=('Courier', 10), justify='center')
    var.set('Welcome')
    label1.place(x=75, y=150)

    # btn1 = Button(text='Start', bg='#000', command=runAssistant, image=updatedStartButtonImage)
    # btn1.config(font=("Courier", 12))
    # btn1.place(x=75, y=275)

    # btn2 = Button(text='EXIT', bg='#000', command=exitAssistant, image=updatedExitButtonImage)
    # btn2.config(font=("Courier", 12))
    # btn2.place(x=425, y=275)

    window.title('David')

    # Call runAssistant method directly here
    runAssistant()

    window.mainloop()

