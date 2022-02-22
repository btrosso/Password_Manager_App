from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

DEFAULT_FONT = ("Arial", 10, "normal")
# ---------------------------- SEARCH FUNCTION ---------------------------------- #
def search_saved_data():
    site = web_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No File Found", message="There has been no data saved yet.")
    else:
        if site in data:
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=f"{site}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=f"{site}", message="No saved data found for this website.")
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
    site = web_entry.get().title()
    email_user = user_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            "email": email_user,
            "password": password
        }
    }

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # if there was no file found we create one and dump the new_data into it
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the old data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
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
web_entry.grid(column=1, row=1, sticky="ew")
web_entry.focus()

user_entry = Entry()
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
user_entry.insert(0, "example@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="ew")

# buttons
gen_button = Button(text="Generate Password", command=gen_password)
gen_button.grid(column=2, row=3, sticky="ew")

search_button = Button(text="Search", command=search_saved_data)
search_button.grid(column=2, row=1, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()