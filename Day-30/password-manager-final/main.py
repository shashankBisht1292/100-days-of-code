from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    try:
        with open("./data.json", "r") as read_file:
            data = json.load(read_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File found.")
    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(website, f"Email:{data[website]['email']}\n Password: {data[website]['password']}")
        else:
            messagebox.showerror("Error", f"No details for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    email_uname = email_uname_entry.get()
    password = password_entry.get()

    if website == "" or email_uname == "" or password == "":
        messagebox.showerror("Error", "Please fill all required fields.")
    else:
        new_data = {
            website: {
                "email": email_uname,
                "password": password
            }
        }
        try:
            with open("./data.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            with open("./data.json", "w") as write_file:
                json.dump(new_data, write_file, indent=4)
        else:
            data.update({website: {"email": email_uname, "password": password}})
            with open("./data.json", "w") as write_file:
                json.dump(data, write_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_uname_entry.delete(0, END)
            email_uname_entry.insert(0, "abcd@gmail.com")
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
Label(text="Website:", bg="white").grid(row=1, column=0)
Label(text="Email/Username:", bg="white").grid(row=2, column=0)
Label(text="Password:", bg="white").grid(row=3, column=0)

#Entry
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_uname_entry = Entry(width=39)
email_uname_entry.insert(END, "abcd@gmail.com")
email_uname_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
Button(text="Search", command=search, width=13).grid(row=1, column=2)
Button(text="Generate Password", command=generate_pass).grid(row=3, column=2)
Button(text="Add", command=add_data, width=36).grid(row=4, column=1, columnspan=2)





window.mainloop()