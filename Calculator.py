from tkinter import *
root=Tk()
root.title("HML Calculator")
Name_Entry = Entry(root,width=45,borderwidth=5)
Name_Entry.grid(column=0,row=0,columnspan=3,padx=20,pady=20)
name=""
first_num=0
def function(number):
    x=Name_Entry.get()
    Name_Entry.delete(0,END)
    Name_Entry.insert(0,str(x)+str(number))
def add_function():
    global name
    name="Addition"
    global first_num
    first_num=int(Name_Entry.get())
    Name_Entry.delete(0,END)
def subtract_function():
    global name
    name ="Subtraction"
    global first_num
    first_num= int(Name_Entry.get())
    Name_Entry.delete(0, END)
def multiply_function():
    global name
    name ="Multiplication"
    global first_num
    first_num = int(Name_Entry.get())
    Name_Entry.delete(0, END)
def divide_function():
    global name
    name ="Division"
    global first_num
    first_num = int(Name_Entry.get())
    Name_Entry.delete(0,END)
def equal_function():
    if name=="Addition":
        z=Name_Entry.get()
        Name_Entry.delete(0,END)
        Name_Entry.insert(0,first_num+int(z))
    if name=="Subtraction":
        z = Name_Entry.get()
        Name_Entry.delete(0, END)
        Name_Entry.insert(0, first_num - int(z))
    if name=="Multiplication":
        z = Name_Entry.get()
        Name_Entry.delete(0, END)
        Name_Entry.insert(0, first_num * int(z))
    if name=="Division":
        z = Name_Entry.get()
        Name_Entry.delete(0, END)
        Name_Entry.insert(0, first_num / int(z))
def clear_function():
    Name_Entry.delete(0,END)
num_zero=Button(root,text='0',padx=40,pady=20,command=lambda: function(0))
num_one=Button(root,text='1',padx=40,pady=20,command=lambda: function(1))
num_two=Button(root,text='2',padx=40,pady=20,command=lambda: function(2))
num_three=Button(root,text='3',padx=41,pady=20,command=lambda: function(3))
num_four=Button(root,text='4',padx=41,pady=20,command=lambda: function(4))
num_five=Button(root,text='5',padx=41,pady=20,command=lambda: function(5))
num_six=Button(root,text='6',padx=41,pady=20,command=lambda: function(6))
num_seven=Button(root,text='7',padx=41,pady=20,command=lambda: function(7))
num_eight=Button(root,text='8',padx=41,pady=20,command=lambda: function(8))
num_nine=Button(root,text='9',padx=41,pady=20,command=lambda: function(9))
add_button=Button(root,text='+',padx=92,pady=20,command=add_function)
equal_button=Button(root,text='=',padx=92,pady=20,command=equal_function)
clear_button=Button(root,text="Clear",padx=30,pady=20,command=clear_function)
subtract_button=Button(root,text="-",padx=41,pady=20,command=subtract_function)
multiply_button=Button(root,text="*",padx=41,pady=20,command=multiply_function)
divide_button=Button(root,text="/",padx=41,pady=20,command=divide_function)
num_zero.grid(column=0,row=1)
num_one.grid(column=1,row=1)
num_two.grid(column=2,row=1)
num_three.grid(column=0,row=2)
num_four.grid(column=1,row=2)
num_five.grid(column=2,row=2)
num_six.grid(column=0,row=3)
num_seven.grid(column=1,row=3)
num_eight.grid(column=2,row=3)
num_nine.grid(column=0,row=4)
add_button.grid(column=1,row=4,columnspan=3)
equal_button.grid(column=1,row=5,columnspan=2)
clear_button.grid(column=0,row=5)
subtract_button.grid(column=0,row=6)
multiply_button.grid(column=1,row=6)
divide_button.grid(column=2,row=6)





root['background']='#856ff8'
root.mainloop()