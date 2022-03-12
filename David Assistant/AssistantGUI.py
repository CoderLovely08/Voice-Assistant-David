from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.geometry('800x800')
window.minsize(630,395)
window.maxsize(630,395)

global var
global var1

var = StringVar()
var1 = StringVar()

labelImage=Image.open('images/labelBackground.jpg')
resizedLableImage=labelImage.resize((200,50),Image.ANTIALIAS)
updatedLabelImage=ImageTk.PhotoImage(resizedLableImage)

startButtonImage=Image.open('images/Start.png')
resizedStartImage=startButtonImage.resize((125,40),Image.ANTIALIAS)
updatedStartButtonImage=ImageTk.PhotoImage(resizedStartImage)

ExitButtonImage=Image.open('images/Quit.png')
resizedExitImage=ExitButtonImage.resize((125,40),Image.ANTIALIAS)
updatedExitButtonImage=ImageTk.PhotoImage(resizedExitImage)

backgroundImage=Image.open('images/back1.png')
resizedBackgroundImage=backgroundImage.resize((630,395),Image.ANTIALIAS)
updatedBackgroundImage=ImageTk.PhotoImage(resizedBackgroundImage)

bglabel=Label(window,image=updatedBackgroundImage)
bglabel.place(x=0,y=0)


label2 = Message(window, textvariable=var1,width=450,fg='#0f0',bg='#000',font=('Courier',10))
var1.set('User Said:')
label2.place(x=75,y=75)

label1 = Message(window, textvariable=var,width=450,fg='#00ff00',bg='#000',font=('Courier',10),justify='center')
var.set('Welcome')
label1.place(x=75,y=150)

btn1 = Button(text='Start', bg='#000', padx=20,image=updatedStartButtonImage)
btn1.config(font=("Courier", 12))
btn1.place(x=75,y=275)

btn2 = Button(text='EXIT', bg='#000', padx=20,image=updatedExitButtonImage)
btn2.config(font=("Courier", 12))
btn2.place(x=425,y=275)

window.title('JARVIS')
window.mainloop()
