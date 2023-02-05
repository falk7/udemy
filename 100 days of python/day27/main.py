from tkinter import *

window = Tk()
window.title("my 1st screen")
window.minsize(width=600, height=300)

def button_click():
    text = entry.get()
    mylbl.config(text=text )

mylbl=Label(text="this is a label")
mylbl.grid(column=0, row=0)

button = Button(text="Click me", command=button_click)
button.grid(column=1,row=1)

button2 = Button(text="Click me", command=button_click)
button2.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()