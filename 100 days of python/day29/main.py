from tkinter import *
from tkinter import messagebox
import pyperclip
WHITE = "#fff"
PASSWORT_LENGTH = 40
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password() -> str:
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = PASSWORT_LENGTH // 3 * 2
    nr_symbols = PASSWORT_LENGTH // 3 // 2
    nr_numbers = PASSWORT_LENGTH // 3 // 2

    password_list = []

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password() -> None:
    website = entry_website.get()
    mail = entry_mail.get()
    password = entry_password.get()

    if website == "" or mail == "" or password == "":
        messagebox.showerror(title="Feld leer!",
                             message="Eins der Felder ist leer, Junge!")
        return

    is_ok = messagebox.askokcancel(
        title=website, message=f"Das wird für {website} gespeichert:\nEmail: {mail}\nPassword: {password}\nGeht das klar!?")

    if is_ok:
        with open("data.txt", mode="a", encoding="UTF-8")as file:
            file.write(f"{website} | {mail} | {password}\n")

        entry_website.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = Entry(width=45)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_mail = Entry(width=45)
entry_mail.insert(END, string="falk.altrock@gmail.com")
entry_mail.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=25)
entry_password.grid(column=1, row=3)


button_generate = Button(text="Generate Password",
                         command=generate_password)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", command=save_password, width=40)
button_add.grid(column=1, columnspan=2, row=4)

window.mainloop()
