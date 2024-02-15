from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    pass_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Add letters, numbers, and symbols to the list
    pass_letters = [choice(letters) for i in range(randint(8,10))]
    pass_numbers = [choice(numbers) for i in range(randint(3,5))]
    pass_symbols = [choice(symbols) for i in range(randint(3,5))]

    password_list= pass_numbers + pass_symbols + pass_letters
    # Shuffle the list
    shuffle(password_list)

    # Convert the list back to a string
    password_str = ''.join(password_list)
    pass_entry.insert(INSERT, password_str)
    pyperclip.copy(password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    passw = pass_entry.get()

    if len(website) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops", message="Please enter data into all fields")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"These are the details entered. \n Email: {email} \n Password: {passw}\n Is it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {passw}\n")
            web_entry.delete(0, "end")
            pass_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Arial", 12))
website.grid(column=0, row=1)  # Position the label in the grid

email = Label(text="Email/Username:", font=("Arial", 12))
email.grid(column=0, row=2)  # Position the label in the grid

password = Label(text="Password:", font=("Arial", 12))
password.grid(column=0, row=3)  # Position the label in the grid

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky=E + W)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(INSERT, "me@myemail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky=E + W)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky=E + W)

gen_button = Button(text="Generate Password", command=gen_pass)
gen_button.grid(column=2, row=3, sticky=E + W)  # Position the button in the grid

add_button = Button(text="Add Credentials", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=E + W)  # Position the button in the grid

window.mainloop()
