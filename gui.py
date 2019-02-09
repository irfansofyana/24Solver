from tkinter import *
from random import *
import tkinter.messagebox

#-------------------------------------------- Back End --------------------------------------------------------------------


op = ["+","-","*","/"]
global solution
mini = 0
idx = 0

def Compute(b1, ch, b2):
	return eval(str(b1)+ch+str(b2))

def Diff(bil):
	return abs(24-bil)

def PrintSolution(bil, solution):
	tmp = ""
	for i in range(0, 4):
		if (i <= 2):
			tmp = tmp+str(bil[i])+solution[i]
			print(bil[i],solution[i], end=" ")
		else:
			tmp = tmp + str(bil[3])
			print(bil[3])
	print(eval(tmp))
	

def Solve(bil):
	bil.sort(reverse = True)
	if (Diff(bil[0]+bil[1]) <= Diff(bil[0]*bil[1])):
		#+ _ _
		solution.append("+")
		curr = bil[0] + bil[1]
		if (curr <= 24):
			solution.append("+")
			for j in range(0, 5):
				if (j <= 3):
					tmp = Compute(bil[2], op[j], bil[3])
				else:
					tmp = Compute(bil[3], op[3], bil[2])
				tmp = curr + tmp
				if (j == 0):
					mini = Diff(tmp)
					idx = j
				elif (Diff(tmp) < mini):
					mini = Diff(tmp)
					idx = j
			if (idx == 4):
				solution.append(op[3])
			else:
				solution.append(op[idx])
			if (idx == 4):
				bil[2], bil[3] = bil[3], bil[2]
			PrintSolution(bil, solution)
		else:
			for j in range(0, 5):
				if (j == 0):
					tmp = bil[2]+bil[3]
				elif (j == 1):
					tmp = bil[2]-bil[3]
				elif (j == 2):
					tmp = bil[3]-bil[2]
				elif (j == 3):
					tmp = bil[2]/bil[3]
				else:
					tmp = bil[3]/bil[2]
				tmp = curr - tmp;
				if (j == 0):
					mini = Diff(tmp)
					idx = j
				elif (Diff(tmp) < mini):
					mini = Diff(tmp)
					idx = j
			solution.append("-")
			if (idx == 0):
				solution.append("-")
			elif (idx == 1 or idx == 2):
				solution.append("+")
			elif (idx == 3 or idx == 4):
				solution.append("/")
			if (idx == 4 or idx == 2):
				bil[2], bil[3] = bil[3], bil[2]
			PrintSolution(bil, solution)
	else:
		#* _ _
		solution.append("*")
		curr = bil[0] * bil[1]
		for j in range(0, 2):
			for i in range(0, 4):
				tmp = Compute(curr, op[i], bil[j+2])
				if (i == 0):
					mini = Diff(tmp)
					idx = i
				elif (Diff(tmp) < mini):
					mini = Diff(tmp)
					idx = i
			solution.append(op[idx])
			if (j == 0):
				curr = Compute(curr, op[idx], bil[2])
				prv = idx
		if (idx == 2 or idx == 3):
			if (prv == 0 or prv == 1):
				print("(", bil[0], solution[0], bil[1], solution[1], bil[2], ")", solution[2], bil[3])
				print(eval("("+str(bil[0])+solution[0]+str(bil[1])+solution[1]+str(bil[2])+")"+solution[2]+str(bil[3])))
			else:
				PrintSolution(bil, solution)
		else:
			PrintSolution(bil, solution)



#Langkah-langkah greedy:
#Strategi greedy : Pilih operator yang menghasilkan nilai sedekat mungkin dengan 24
#Langkah optimal disini adalah langkah yang menghasilkan nilai sedekat mungkin dengan 24

#1. Pertama sort empat bilangan tersebut secara descending (b[0] >= b[1] >= b[2] >= b[3])
#2. Selanjutnya kita pilih mana yg lebih optimal antara memilih (b[0] + b[1]) atau (b[0]*b[1])
#3. Apabila di langkah kedua lebih optimal untuk menggunakan '+', maka akan ada beberapa kemungkinan:
#		3.1.1 jumlah b[0]+b[1] <= 24
#			Maka langkah optimal yang harus kita lakukan adalah menambah bilangan ini dengan bilangan hasil operasi 
#			b[2] dan b[3]. Yang mungkin hanya menambah dengan b[2]+b[3], b[2]-b[3], b[2]*b[3], b[2]/b[3] atau b[3]/b[2]
#			Pilih mana yang paling mendekati hasilnya dengan 24
#		3.1.2 jumlah b[0]+b[1] > 24
#			Maka langkah optimal yang harus kita lakukan adalah mengurangi bilangan ini dengan bilangan hasil operasi b[2]
#			dan b[3]. Yang mungkin adalah menguranginya dengan (b[2]+b[3]), (b[2]-b[3]), (b[3]-b[2]), (b[2]/b[3]), dan (b[3]/b[2]). 
#			Pilih mana yang paling mendekati hasilnya dengan 24
#	Apabila di langkah kedua lebih optimal untuk menggunakan '*', maka kita harus mengecek dua operator berikutnya mana yang 
#   paling optimal. Perlu hati-hati dikasus ini adalah ketika kita memakai operator '+' lalu operator '*', maka kita harus memakai
#	kurung

#-------------------------------------------- Front End --------------------------------------------------------------------

def new():
    print("New")

def quit():
    answer = tkinter.messagebox.askyesno('Quit Prompt',"Are you sure you want to quit?")
    if(answer == YES):
        root.quit()

def howtouse():
    print("How to use")

def shuffledeck():
    shuffle(cardsdeck)

def newround():
    global solution
    if (len(cardsdeck) == 0):
        print("Abis gan")
    else:
        shuffledeck()    
        cards = [cardsdeck[0],cardsdeck[1],cardsdeck[2],cardsdeck[3]]
        cardsdeck.remove(cards[0])
        cardsdeck.remove(cards[1])
        cardsdeck.remove(cards[2])
        cardsdeck.remove(cards[3])
        print(cards)
        updatecards(cards[0], 0)
        updatecards(cards[1], 1)
		updatecards(cards[2], 2)
		updatecards(cards[3], 3)
		bil = [0,0,0,0]
		solution = []
		for x in range(4):
			bil[x] = getcardvalue(cards[x])
		Solve(bil)
		op1.config(text = solution[0])

def getcardvalue(a):
    if(a[0] == 'A'):
        return(1)
    elif(a[0] == '2'):
        return(2)
    elif(a[0] == '3'):
        return(3)
    elif(a[0] == '4'):
        return(4)
    elif(a[0] == '5'):
        return(5)
    elif(a[0] == '6'):
        return(6)
    elif(a[0] == '7'):
        return(7)
    elif(a[0] == '8'):
        return(8)
    elif(a[0] == '9'):
        return(9)
    elif(a[0] == '1'):
        return(10)
    elif(a[0] == 'J'):
        return(11)
    elif(a[0] == 'Q'):
        return(12)
    elif(a[0] == 'K'):
        return(13)

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


cardsdeck = ['2D','2C','2H','2S','3D','3C','3H','3S','4D','4C','4H','4S','5D','5C','5H','5S',
             '6D','6C','6H','6S','7D','7C','7H','7S','8D','8C','8H','8S','9D','9C','9H','9S',
             '10D','10C','10H','10S','AD','AC','AH','AS','JD','JC','JH','JS','QD','QC','QH','QS',
             'KD','KC','KH','KS']

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

