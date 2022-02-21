from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

DEFAULT_FONT = ("Arial", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    current_value_of_entry = password_entry.get()

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    if len(current_value_of_entry) == 0:
        password_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = web_entry.get()
    email_user = user_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {email_user}\n"
                                                   f"Password: {password}\nIs it okay to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{site} | {email_user} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

# create the window and configure it
window = Tk()
window.title("Password Manager")
window.config(bg="black", width=200, height=200, padx=20, pady=20)

# create the canvas and configure it
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
web_label = Label(text="Website:", bg="black", fg="white", font=DEFAULT_FONT)
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", bg="black", fg="white", font=DEFAULT_FONT)
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="black", fg="white", font=DEFAULT_FONT)
password_label.grid(column=0, row=3)

# entries
web_entry = Entry()
web_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
web_entry.focus()

user_entry = Entry()
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
user_entry.insert(0, "example@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="ew")

# buttons
gen_button = Button(text="Generate Password", command=gen_password)
gen_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()