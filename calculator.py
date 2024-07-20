import tkinter as tk
from tkinter import messagebox

def get_sum():
    #Get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())

    result = value1 + value2
    messagebox.showinfo("Result", f"The sum is {result}")

root = tk.Tk()
root.title("My Calculator")
root.geometry("500x500")

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
button = tk.Button(root, text = "Find sum", command = get_sum)
button.pack(pady = 10)



#Run
root.mainloop()