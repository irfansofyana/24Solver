from proto import *
from tkinter import *
from random import *
import tkinter.messagebox

# global cards

def new():
    print("New")

def quit():
    answer = tkinter.messagebox.askyesno('Quit Prompt',"Are you sure you want to quit?")
    if(answer == YES):
        root.quit()

def howtouse():
    print("How to use")

def newround():
    # global bil
    # global cards
    if (len(cardsdeck) == 0):
        print("Abis gan")
    else:
        shuffledeck()
        updatebil()
        updatecards(cards[0], 0)
        updatecards(cards[1], 1)
        updatecards(cards[2], 2)
        updatecards(cards[3], 3)

def updatecards(a,b):
    stringz = "cards_png/"+a+".png"
    gambar = PhotoImage(file=stringz)
    if(b == 0):
        image1label.configure(image=gambar)
        image1label.image = gambar
        num1.config(text = getcardvalue(a))
    elif(b == 1):
        image2label.configure(image=gambar)
        image2label.image = gambar
        num2.config(text = getcardvalue(a))
    elif(b == 2):
        image3label.configure(image=gambar)
        image3label.image = gambar
        num3.config(text = getcardvalue(a))
    elif(b == 3):
        image4label.configure(image=gambar)
        image4label.image = gambar
        num4.config(text = getcardvalue(a))

root = Tk()
tkinter.messagebox.showinfo('Welcome','Masuk Gan')

#***** Main Menu *****
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu)
mainmenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New..", command=newround)
filemenu.add_separator()
filemenu.add_command(label="Quit..", command=quit)

helpmenu = Menu(mainmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="How to use", command=howtouse)


#***** Body *****
bodyframe = Frame(root, width=1920, height=1080, bg="green")
bodyframe.pack(fill=BOTH)

#*****

#Image Dictionary
imageback = PhotoImage(file="cards_png/Gray_back.png")
image1 = PhotoImage(file="cards_png/AD.png")
image2 = PhotoImage(file="cards_png/AC.png")
image3 = PhotoImage(file="cards_png/AH.png")
image4 = PhotoImage(file="cards_png/AS.png")

#Image in Display
imagebacklabel = Label(bodyframe, image=imageback, height=200, width=131)
imagebacklabel.grid(row=0, column=6, pady=20, padx=20)

image1label = Label(bodyframe, image=image1, height=200, width=131)
image1label.grid(row=1,column=0, pady=20, padx=20)

image2label = Label(bodyframe, image=image2, height=200, width=131)
image2label.grid(row=1,column=2, pady=20, padx=20)

image3label = Label(bodyframe, image=image3, height=200, width=131)
image3label.grid(row=1,column=4, pady=20, padx=20)

image4label = Label(bodyframe, image=image4, height=200, width=131)
image4label.grid(row=1,column=6, pady=20, padx=20)

#Label in Display (row 2)
num1 = Label(bodyframe, text="_")
num1.grid(row=2, column=0)

op1 = Label(bodyframe, text="_")
op1.grid(row=2, column=1)

num2 = Label(bodyframe, text="_")
num2.grid(row=2, column=2)

op2 = Label(bodyframe, text="_")
op2.grid(row=2, column=3)

num3 = Label(bodyframe, text="_")
num3.grid(row=2, column=4)

op3 = Label(bodyframe, text="_")
op3.grid(row=2, column=5)

num4 = Label(bodyframe, text="_")
num4.grid(row=2, column=6)


#***** Status Bar *****
statusbar = Label(root, text="24 Solver", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()