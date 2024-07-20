#Simple level GUI application

import tkinter as tk
 # root is variable
root = tk.Tk()
root.title("Rachin Giri")
root.geometry("750x500")

#Run
def on_button_click():
    label.config(text = "Button Clicked")

label = tk.Label(root, text = "Welcome")
label.pack(pady = 20)

button = tk.Button(root, text = "Click me", command = on_button_click)
button.pack(pady = 10)

root.mainloop()