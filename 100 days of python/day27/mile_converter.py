from tkinter import *

window = Tk()
window.title("miles to kilometers")
window.minsize()
window.config(padx=50, pady=50)

def calculate_kilometers():
    kilometers = float(entry.get()) * 1.6
    lbl_result.config(text=kilometers)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)

lbl_is_equal_to = Label(text="is equal to")
lbl_is_equal_to.grid(column=0,row=1)

lbl_result = Label(text="0")
lbl_result.grid(column=1, row=1)

lbl_km = Label(text="Km")
lbl_km.grid(column=2, row=1)

btn_calc = Button(text="Calculate", command=calculate_kilometers)
btn_calc.grid(column=1,row=2)





window.mainloop()