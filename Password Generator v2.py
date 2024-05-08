import random
from tkinter import messagebox
from tkinter import * # pip install tk

def generate_password(): # Function to generate password
    try:
        length = int(length_entry.get()) # Get length from entry
    except:
        messagebox.showerror(message="Please enter a valid length.") # Show error if invalid length
        return

    password = random.choices(character_string, k=length) # Generate password
    password = ''.join(password)
 
    password_v.set(password)

character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!(),-./:?_" # Characters to be used in password

password_gen  = Tk() # Create a window
password_gen.geometry("350x200")
password_gen.title("Password Generator")
password_gen.configure(bg="#164558")

title_label = Label(password_gen, text="Password Generator", font=('Calibri', 18), bg="#164558", fg="white")  # Label for title
title_label.pack()

length_label = Label(password_gen, text="Required length: ", bg="#164558", fg="white", font=('Calibri', 12))  # Label for length
length_label.place(x=95, y=50)
length_entry = Entry(password_gen, width=3, bg="white", fg="black", font=('Calibri', 12))  # Entry for length
length_entry.place(x=200, y=50)  

password_v = StringVar() # Variable to store password
password_label = Entry(password_gen, bd=0, bg="#000000", textvariable=password_v, state="readonly", fg="white", font=('Calibri', 12), width=35)  # Label for password
password_label.place(x= 30, y=150)  

password_button = Button(password_gen, text="Generate Password", command=generate_password, fg="black", font=('Calibri', 12)) # Button to generate password
password_button.place(x= 100, y=100)  

password_gen.mainloop()
