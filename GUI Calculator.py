from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator")
root.iconbitmap("D:/Documents/Python-Projects/Calculator/Dtafalonso-Android-Lollipop-Calculator.ico")

# entry
display = Entry(root, width=45, borderwidth=5)
display.grid(column=0, row=0, columnspan=3, padx=10, pady=10)


# Buttons Actions
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))


def button_clear():
    display.delete(0, END)


def button_addition():
    first_num = display.get()
    global mamory
    global math
    math = "+"
    mamory = int(first_num)
    display.delete(0, END)


def button_subtraction():
    first_num = display.get()
    global mamory
    global math
    math = "-"
    mamory = int(first_num)
    display.delete(0, END)


def button_multiplication():
    first_num = display.get()
    global mamory
    global math
    math = "*"
    mamory = int(first_num)
    display.delete(0, END)


def button_division():
    first_num = display.get()
    global mamory
    global math
    math = "/"
    mamory = int(first_num)
    display.delete(0, END)


def button_equal():
    second_num = display.get()
    display.delete(0, END)
    if math == "+":
        display.insert(0, mamory + int(second_num))
    elif math == "-":
        display.insert(0, mamory - int(second_num))
    elif math == "*":
        display.insert(0, mamory * int(second_num))
    elif math == "/":
        display.insert(0, mamory / int(second_num))


# creating Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_pl = Button(root, text="+", padx=40, pady=20, command=button_addition)
button_mi = Button(root, text="-", padx=40, pady=20, command=button_subtraction)
button_ex = Button(root, text="*", padx=40, pady=20, command=button_multiplication)
button_de = Button(root, text="/", padx=40, pady=20, command=button_division)
button_eq = Button(root, text="=", padx=90, pady=20, command=button_equal)
button_cl = Button(root, text="Clear", padx=80, pady=20, command=button_clear)

# Update to display
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=6, column=0)

button_pl.grid(row=1, column=0)
button_mi.grid(row=1, column=1)
button_ex.grid(row=1, column=2)

button_de.grid(row=2, column=0)
button_cl.grid(row=2, column=1, columnspan=3)
button_eq.grid(row=6, column=1, columnspan=3)

root.mainloop()
