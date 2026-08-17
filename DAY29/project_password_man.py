from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
# ----------------------------PASSWORD GENERATOR------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    #list comprehension
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _  in range(randint(2,4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)#here we used join method
    pass_input.insert(0,password)
    pyperclip.copy(password)
# ----------------------------SAVE PASSWORD------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="please dont left any of field empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail: {email}\npassword: {password} \nIs it ok to save")
        if is_ok:
            with open("DAY29//data.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")

            #Clear the entries
            web_input.delete(0,END)
            email_input.delete(0,END)
            pass_input.delete(0,END)
            web_input.focus()
            #add default email again
            email_input.insert(0,"xyz@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)
#canvas
canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="DAY29//logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

#labels

#webise label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
#email/username
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
#password label 
pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)
 

#Entries
#web input
web_input = Entry(width=52)
web_input.grid(row=1,column=1,columnspan=2)
web_input.focus()
#email input
email_input = Entry(width=52)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0," xyz@gmail.com")#this holds the default value at the entry
#pass input 
pass_input = Entry(width=33)
pass_input.grid(row=3, column=1)

#BUTTONS
#Generate button 
button = Button(text="Generate Password",command=password_generate)
button.grid(row=3,column=2)
#Add button
add_button = Button(text="Add",width=44, command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()
