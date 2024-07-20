	
#Create a visually appealing program using Python's tkinter library.
#  that calculates the sum, difference, product, and quotient of two user-entered numbers.

import tkinter as tk
from tkinter import messagebox


def get_sum():
    #Get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    result = value1 + value2
    messagebox.showinfo("Result", f"The {value1} + {value2} is {result}")

def get_difference():
    #Get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    result = value1 - value2
    messagebox.showinfo("Result", f"The {value1} - {value2} is {result}")

def get_product():
    #Get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    result = value1 * value2
    messagebox.showinfo("Result", f"The {value1} * {value2}  is {result}")

def get_quotient():
    #Get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    result = value1 % value2
    messagebox.showinfo("Result", f"The {value1} % {value2}  is {result}")

root = tk.Tk()
root.title("My Calculator")
root.geometry("500x500")
root.config(bg = "Black")  #GUI background color

#For first Number
label1 = tk.Label(root, text ="Enter first number: ")
label1.pack(pady = 5)
entry1 = tk.Entry(root)
entry1.pack(pady = 5)

#For Second no.
label2 = tk.Label(root, text ="Enter second number: ")
label2.pack(pady = 5)
entry2 = tk.Entry(root)
entry2.pack(pady = 5)

#Button
button1 = tk.Button(root, text = "+", command = get_sum)
button1.pack(pady = 10)

button2 = tk.Button(root, text = "-", command = get_difference)
button2.pack(pady = 10)

button3 = tk.Button(root, text = "*", command = get_product)
button3.pack(pady = 10)

button3 = tk.Button(root, text = "%", command = get_quotient)
button3.pack(pady = 10)



#Run
root.mainloop()