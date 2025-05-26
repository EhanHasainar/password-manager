import random
import tkinter

YOUREMAIL = 'email@gmail.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = 8
    nr_symbols = 2
    nr_numbers = 2

    password = ""
    while nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0:
        x = random.randint(0, 2)
        if x == 0 and nr_letters > 0:
            password += random.choice(letters)
            nr_letters -= 1
        elif x == 1 and nr_symbols > 0:
            password += random.choice(symbols)
            nr_symbols -= 1
        elif x == 2 and nr_numbers > 0:
            password += random.choice(numbers)
            nr_numbers -= 1

    password_text.delete(0, tkinter.END)
    password_text.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if not website or not email or not password:
        tkinter.messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return
    
    is_ok = tkinter.messagebox.askokcancel(title='website', message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        website_text.delete(0, tkinter.END)
        email_text.delete(0, tkinter.END)
        password_text.delete(0, tkinter.END)
# ---------------------------- UI SETUP ------------------------------- #
FONT = ("Arial", 10)
BUTTON_FONT = ("Arial", 7)

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, padx=2, pady=2, sticky="e")

website_text = tkinter.Entry(width=32, font=FONT)
website_text.grid(column=1, row=1, columnspan=2, sticky="ew", padx=2, pady=2)
website_text.focus()

email_label = tkinter.Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2, padx=2, pady=2, sticky="e")

email_text = tkinter.Entry(width=32, font=FONT)
email_text.grid(column=1, row=2, columnspan=2, sticky="ew", padx=2, pady=2)
email_text.insert(0, YOUREMAIL)

password_label = tkinter.Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, padx=2, pady=2, sticky="e")

password_text = tkinter.Entry(width=21, font=FONT)
password_text.grid(column=1, row=3, sticky="ew", padx=(2, 0), pady=2)

generate_button = tkinter.Button(text="Generate Password", font=BUTTON_FONT, command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew", padx=(2, 2), pady=2, ipady=0)

add_button = tkinter.Button(text="Add", font=FONT, command=save)
add_button.grid(column=1, row=4, columnspan=2, padx=2, pady=2, sticky="ew")

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
