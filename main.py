import tkinter
from tkinter import *
import random
from tkinter import messagebox
import pyperclip
from random import choice,shuffle,randint


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Fields Empty!!")
    else:
        try:
            with open("user_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("user_data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                clear()
        else:
            data.update(new_data)
            with open("user_data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            clear()

def clear():
    web_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)
    web_input.focus()

#-----------------------------Search-----------------------------------#

def search():
    website = web_input.get()
    try:
        with open("user_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No file found")
    else:
        if website in data:
            ##1 way to do it
            # web_data = data[f"{website}"]
            # email = web_data["email"]
            # password = web_data["password"]

            #Better way:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="confirm", message=f"Email:{email}\nPassword:{password}")
            email_input.delete(0, END)
            password_input.delete(0, END)
            email_input.insert(0, email)
            password_input.insert(0, password)
        elif website not in data:
            messagebox.showinfo(title="oops", message="Data not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website
web_label = Label(text="Website", font=("Poppins", 15))
web_label.grid(row=1, column=0, sticky="E", padx=(0, 10))
#WebsiteEntry
web_input = tkinter.Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2, sticky="W")
web_input.focus()

# Email
email_label = Label(text="Email", font=("Poppins", 15))
email_label.grid(row=2, column=0, sticky="E", padx=(0, 10))

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="W")
email_input.insert(0, "Enter your email")

# Password
password_label = Label(text="Password", font=("Poppins", 15))
password_label.grid(row=3, column=0, sticky="E", padx=(0, 10))

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1, sticky="W")

#Buttons
generate_button = Button(text="Generate", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

search_button = Button(text="Search", width=5, command=search)
search_button.grid(row=1, column=2, sticky="E")
window.mainloop()
