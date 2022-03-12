'''from keyboard import press, press_and_release
import time

def chromeAuto(query):
      time.sleep(5)
      if "new tab" in query:
            press_and_release("ctrl + t")
      elif "close tab" in query:
            print('closing tab')
            press_and_release("ctrl + w")
      elif "new window" in query:
            press_and_release("ctrl+n")
      elif "history" in query:
            press_and_release("ctrl+h")
      elif "download" in query:
            press_and_release("ctrl+j")
query=input("Enter your command")
chromeAuto(query)'''
import threading
import webbrowser

import googlesearch
import pyautogui
import volux



'''elif "david" in query:
            generalResponse()'''

import time
from pyautogui import *
from keyboard import *
from time import *
import os
from datetime import datetime
'''sleep(5)
var=pyautogui.position()
print(var)
'''

'''elif 'alarm' in query:
print("enter the time")
getAlarmTime = input("enter the time")

while True:
    Time_Ac = datetime.datetime.now()
    now = Time_Ac.strftime("%H:%M:%S")

    if now == time:
        print("time to wake up sir")
        # playsound()
        print("alarm closed!")

    elif now > time:
        break

'''

'''from generalResponse import responseDictionary
while True:
    user=input("Enter you command: ")
    query=responseDictionary
    if user in query.keys():
        print(query[user])
'''
'''elif "where is" in query:
query = query.replace("where is", "")
location = query
print("User asked to Locate")
print(location)
webbrowser.open("https://www.google.nl / maps / place/" + location + "")'''

'''def volumeControl(changeVolumeCommand):
    try:
        getCurrentBrightnest=sbc.get_volume()
        volumeLevel=getIntegers(changevolumeCommand)
        if "increase" in changevolumeCommand:
            sbc.set_volume(getCurrentBrightnest + volumeLevel)
            print(f"volume increased by {volumeLevel}%")
        else:
            sbc.set_volume(getCurrentBrightnest - volumeLevel)
            print(f"volume decreased by {volumeLevel}%")
    except:
        print("Error occurred while changing volume level")
'''
'''import screen_brightness_control as sbc
def getIntegers(string):
    try:
        if '%' in string:
            string=string.replace('%','')
        numbers=[int(word) for word in string.split() if word.isdigit()]
        return numbers[0]
    except:
        return []

#increases and decreases brightness as per user commmnd
def brightnessControl(changeBrightnessCommand):
    try:
        if len(getIntegers(changeBrightnessCommand)) == 0:
            brightnessLevel = 5
        else:
            brightnessLevel = getIntegers(changeBrightnessCommand)

        getCurrentBrightness=sbc.get_brightness()
        if "increase" in changeBrightnessCommand:
            sbc.set_brightness(getCurrentBrightness + brightnessLevel)
            print(f"Brightness increased by {brightnessLevel}%")

        else:
            sbc.set_brightness(getCurrentBrightness - brightnessLevel)
            print(f"Brightness decreased by {brightnessLevel}%")
    except:
        print("Error occurred while changing brightness level")
'''

'''def getIntegers(string):
    try:
        if '%' in string:
            string=string.replace('%','')
        numbers=[int(word) for word in string.split() if word.isdigit()]
        return numbers[0]
    except:
        return []

def changeVolume(string):

    getValue=getIntegers(string)
    taps=int(getValue/10)*5
    if 'up' in string or "increase" in string:
        for i in range(taps):
            pyautogui.press('volumeup')
    elif 'down' in string or 'decrease' in string or "lower" in string:
        for i in range(taps):
            pyautogui.press('volumedown')
changeVolume('decrease volume by 20%')'''


'''from tkinter import *

root = Tk()


def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""

    result =
    for i in range(5):
        var=resultLabel.cget('text')+"\n"+result
        resultLabel.config(text=var)
        sleep(1)

# Create the Entry widget

# Create the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry)
enterEntry.pack(fill=X)

# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)


root.geometry("+750+400")

root.mainloop()'''

from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman
# from Class1 import Student
# import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mridu\AppData\Local\Tesseract-OCR\tesseract.exe"

'''
elif 'read the photo' in query: #If you have Pytesseract installed for Optical Character Recognition
    try:
        im = Image.open('pic.jpg')
        text = pytesseract.image_to_string(im)
        speak(text)
    except Exception as e:
        print("Unable to read the data")
        print(e)
    '''
import wolframalpha
'''def getIntegers(string):
    try:
        if '%' in string:
            string=string.replace('%','')
        numbers=[int(word) for word in string.split() if word.isdecimal()]
        print(numbers)
        return numbers[0]
    except:
        return []

def setTimer(query):
    getTimeinNumbers=getIntegers(query)
    print(getTimeinNumbers)
    print(f"Setting timer for {getTimeinNumbers} seconds")
    sleep(getTimeinNumbers)
    print("Timer complete")

t1=threading.Thread(target=setTimer("set a timer for 10")).start()'''


'''import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                speak(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    speak(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        speak('It\'s a tie!')

def startGame():
    x_player = SmartComputerPlayer('x')
    o_player = HumanPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)



import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            speak("it's your turn, input your move")
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                speak('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

'''
'''import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
'''
'''import time
from plyer import notification

if __name__ == "__main__":

    notification.notify(
        title = "warning....",
        message = "its time to take break",
        timeout=5)
    time.sleep(1)'''
import requests
from bs4 import BeautifulSoup
def getIntegers(string):
    try:
        if '%' in string:
            string = string.replace('%', '')
        if '°C' in string:
            string = string.replace('°C', '')
        numbers = [int(word) for word in string.split() if word.isdigit()]
        return numbers[0]
    except:
        return []
query="temperature in"
if "temperature" in query:
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
                print(f"current {search} is {temp}")
        except:
            print("City not found, please check the city name and try again")
    except:
            print("City not found, please check the city name and try again")