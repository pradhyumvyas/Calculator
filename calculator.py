from tkinter import *

# Creating a window frame
root = Tk()
root.title("Calculator")

ent = Entry(root,width=35, borderwidth=5)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

# Functioning of buttons

def myButton(number):
    temp = ent.get()
    ent.delete(0, END)
    ent.insert(0,str(temp)+str(number))

def myButton_clear():
    ent.delete(0,END)

def myButton_rmv():
    check = len(ent.get())
    ent.delete(check-1)

def myButton_add():
    first_number = ent.get()
    global f_num
    global maths
    maths="Addition"
    f_num = (first_number)
    ent.delete(0, END)

def myButton_sub():
    first_number = ent.get()
    global f_num
    global maths
    maths="Subtraction"
    f_num = (first_number)
    ent.delete(0, END)

def myButton_multi():
    first_number = ent.get()
    global f_num    
    global maths
    maths="Multiplication"
    f_num = (first_number)
    ent.delete(0, END)

def myButton_div():
    first_number = ent.get()
    global f_num    
    global maths
    maths="Division"
    f_num = (first_number)
    ent.delete(0, END)

def myButton_mod():
    first_number = ent.get()
    global f_num
    global maths
    maths = "Modulo"
    f_num = first_number
    ent.delete(0, END)


def myButton_equal():
    second_number = ent.get()
    ent.delete(0,END)

    if maths == "Addition":
        ent.insert(0,float(f_num)+float(second_number))

    elif maths == "Subtraction":
        ent.insert(0,float(f_num)-float(second_number))

    elif maths == "Multiplication":
        ent.insert(0,float(f_num)*float(second_number))

    elif maths == "Division":
        ent.insert(0,float(f_num)/float(second_number))
    
    elif maths == "Modulo":
        ent.insert(0, float(f_num) % float(second_number))


# Button Initialise 
button_1 = Button(root, text="1", padx=30, pady=15, command=lambda:myButton(1))
button_2 = Button(root, text="2", padx=30, pady=15, command=lambda:myButton(2))
button_3 = Button(root, text="3", padx=30, pady=15, command=lambda:myButton(3))

button_4 = Button(root, text="4", padx=30, pady=15, command=lambda:myButton(4))
button_5 = Button(root, text="5", padx=30, pady=15, command=lambda:myButton(5))
button_6 = Button(root, text="6", padx=30, pady=15, command=lambda:myButton(6))

button_7 = Button(root, text="7", padx=30, pady=15, command=lambda:myButton(7))
button_8 = Button(root, text="8", padx=30, pady=15, command=lambda:myButton(8))
button_9 = Button(root, text="9", padx=30, pady=15, command=lambda:myButton(9))

button_0 = Button(root, text="0", padx=30, pady=15, command=lambda:myButton(0))
button_dot = Button(root, text=".", padx=32, pady=15, command=lambda:myButton("."))


# Arthemetic operations

button_add = Button(root, text="+", padx=27, pady=15, command=lambda:myButton_add())
button_sub = Button(root, text="-", padx=30, pady=15, command=lambda:myButton_sub())
button_multi = Button(root, text="*", padx=30, pady=15, command=lambda:myButton_multi())
button_div = Button(root, text="/", padx=30, pady=15, command=lambda:myButton_div())
button_mod = Button(root, text="%", padx=30, pady=15, command=lambda:myButton_mod())

button_equal = Button(root, text="=", padx=30, pady=15, command=lambda:myButton_equal())
button_clear = Button(root, text="C", padx=30, pady=15, command=lambda:myButton_clear())
button_rmv = Button(root, text="<-", padx=26, pady=15, command=lambda:myButton_rmv())

# Button's Grids

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_multi.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_0.grid(row=4,column=1)
button_dot.grid(row=4,column=0)
button_add.grid(row=4,column=3)
button_equal.grid(row=4,column=2)

button_clear.grid(row=5,column=0)
button_rmv.grid(row=5,column=1)
button_mod.grid(row=5,column=2)




# mainloop

root.mainloop()