import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox
import random
#Windows(3)
root=Tk()
#Game1=Tk()....Inside the behaviour
#Game2=Tk()....Inside the behaviour
#global variable
point=0
win=0
lose=0
class Dice_Game:
    def __init__(self,virtual):
        self.virtual=virtual
    def Title(self,title,lab):
        self.virtual.title(title)
        #self.virtual.iconbitmap(r"icon_WG2_icon.ico")
        lbl1 = Label(self.virtual, text=lab, font=('Broadway', 25), fg="White",
                     bg="#000000")
        lbl1.pack()
        lbl2 = Label(self.virtual, text="🎲$🎲$🎲$🎲$🎲$🎲$🎲$🎲$🎲$🎲", font=('Broadway', 25), fg="White", bg="#000000")
        lbl2.pack()
    def Bcolour_Geometry(self,colour,size):
        self.virtual['background']=colour
        self.virtual.geometry(size)
    def Page1_Setup(self):
        Start_button= Button(self.virtual, text="Click here to exchange the points and start the game!",command=lambda: self.Start_button_Command())
        Start_button.pack()
    def Start_button_Command(self):
        global Name_Entry
        Name_Entry = Entry(self.virtual, width=40)
        Name_Entry.place(x=30, y=150)
        Name_Entry.insert(0, "Enter your name and click the button: ")
        Enter = Button(self.virtual, text="Enter", command=lambda: self.Enter_Button_Command())
        Enter.place(x=340, y=150)
    def Enter_Button_Command(self):
        global Name_Entry
        x = Name_Entry.get()
        if x != "Enter your name and click the button: ":
            lbl = Label(self.virtual, text="Hello " + x + " ! Good Luck.", font=("Broadway", 20))
            lbl.place(x=400, y=150)
            lbl3 = Label(self.virtual, text="Enter the amount of money to exchange with points:: 1point=1kyat::",
                         font=("Broadway", 15), fg='Red')
            lbl3.place(x=30, y=200)
            lbl4 = Label(self.virtual, text="During the promotion,you will gain 10% extra point.", font=("Broadway", 15),
                         fg='Red')
            lbl4.place(x=30, y=240)
            global Amount_Money_Entry
            Amount_Money_Entry = Entry(self.virtual, width=45)
            Amount_Money_Entry.place(x=30, y=280, relheight=0.03)
            Amount_Money_Entry.insert(0, "0000")
            Enter2 = Button(self.virtual, text="Exchange", command=lambda: self.Enter2_Button_Command())
            Enter2.place(x=340, y=280)
    def Enter2_Button_Command(self):
        global point
        point = point + int(Amount_Money_Entry.get()) * 10 / 100 + int(Amount_Money_Entry.get())
        if point > 0:
            global lbl5
            lbl5 = Label(self.virtual,text="Good Luck! You exchange " + str(point) + " successfully and you can start playing game.",font=("Broadway", 20))
            lbl5.place(x=30, y=320)
            lbl6 = Label(self.virtual, text="Rules and Description", font=("Broadway", 20), fg='Red')
            lbl6.place(x=30, y=355)
            lbl7 = Label(self.virtual,text="Choose Game Number: \n‣Game 1 is with one die and gain 5x of your chosen point.\n‣Game 2 is with two dice and gain 10x of your chosen point.",font=("Broadway", 15), fg='Black')
            lbl7.place(x=30, y=405)
            Start_button_Game1 = Button(self.virtual, text="Click here to start Game 1",command=lambda: self.Start_button_Game_Command("One"), fg='Red')
            Start_button_Game1.place(x=30, y=480)
            Start_button_Game2 = Button(self.virtual, text="Click here to start Game 2",command=lambda: self.Start_button_Game_Command("Two"), fg='Red')
            Start_button_Game2.place(x=30, y=510)
            Exit_button = Button(self.virtual, text="Exit", command=lambda: self.exit_command(), fg='Black')
            Exit_button.place(x=600, y=600)
    def Start_button_Game_Command(self,Game_name):
        # Game1 Page Setup
        if Game_name=="One":
            Game1 = Tk()
            One=Dice_Game(Game1)
            One.Title("Game1", "Welcome to Dice Game One(🎲)\nGood Luck!")
            One.Bcolour_Geometry('#856ff8',"780x1200")
            One.Game_Startup(1,6,5)
        # Game2 Page Setup
        else:
            Game2 = Tk()
            Two = Dice_Game(Game2)
            Two.Title("Game2", "Welcome to Dice Game Two(🎲🎲)\nGood Luck!")
            Two.Bcolour_Geometry('#856ff8', "780x1200")
            Two.Game_Startup(2,12,10)
    def Game_Startup(self,fro,to,x):
        self.to=to
        self.fro=fro
        global lbl8
        global point
        lbl8 = Label(self.virtual, text="Current points: " + str(point), font=("Broadway", 15), fg='Black')
        lbl8.place(x=30, y=150)
        Bet_Entry = Entry(self.virtual, width=35)
        Bet_Entry.place(x=30, y=190)
        Bet_Entry.insert(0, 'Enter the amount of bet: ')
        lbl10 = Label(self.virtual, text="Guess the number of die 🎲 "+str(fro)+"-"+str(to)+": ", font=("Broadway", 15), fg='Black')
        lbl10.place(x=30, y=220)
        Choose_num = Spinbox(self.virtual, from_=fro, to=to, width=15)
        Choose_num.place(x=30, y=275)
        Roll = Button(self.virtual, text="Roll Now", command=lambda: self.Game_Fuction(int(Bet_Entry.get()), int(Choose_num.get()),x))
        Roll.place(x=340, y=275)
        Exit_button = Button(self.virtual, text="Exit", command=lambda: self.exit_command(), fg='Black')
        Exit_button.place(x=600, y=600)
    def Game_Fuction(self,y,n,x):
        global point
        lbl8.destroy()
        if point >= y:
            point = point - y
            lbl11_2 = Label(self.virtual, text="Rolling the dices...", font=("Broadway", 20), fg='Red')
            lbl11_2.place(x=30, y=300)
            dice_num = random.randint(self.fro,self.to)
            lbl12_2 = Label(self.virtual, text="The value of dice is " + str(dice_num), font=("Broadway", 20))
            lbl12_2.place(x=30, y=345)
            if dice_num == n:
                point += y * x
                self.Display_win_lose("Win")
                lbl5['text'] = "Good Luck! You exchange " + str(point) + " successfully and you can start playing game."
            else:
                self.Display_win_lose("Lose")
                lbl5['text'] = "Good Luck! You exchange " + str(point) + " successfully and you can start playing game."
        else:
            lbl13_2 = messagebox.askquestion("Return", "!!!Click 'Yes' and Exchange More Points!!!")
            if lbl13_2 == 'yes':
                self.virtual.destroy()
    def Display_win_lose(self,condition):
        global win
        global lose
        global lbl14
        global lbl15
        if win==1:
            lbl14.destroy()
        elif lose==1:
            lbl15.destroy()
        if condition == "Win":
            lbl14 = Label(self.virtual, text='You Win!Total points: ' + str(point), font=("Broadway", 20))
            lbl14.place(x=30, y=395)
            win=1
            lose=0
        elif condition == "Lose":
            lbl15 = Label(self.virtual, text="You Lose!Remaining points: "+ str(point), font=("Broadway", 20))
            lbl15.place(x=30, y=395)
            win=0
            lose=1
    def exit_command(self):
        alart = messagebox.askquestion("Waring", "Are you sure to exit?")
        if alart == 'yes':
            self.virtual.destroy()

#Start Page Setup
Start=Dice_Game(root)
Start.Title("Gambling Dice Game","Hello! Welcome to My Gambling Dice Game!")
Start.Page1_Setup()
#Page size and colour
Start.Bcolour_Geometry('#856ff8',"780x1200")
root.mainloop()