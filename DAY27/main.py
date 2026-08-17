from tkinter import *

window = Tk()

window.title("this is my first tkinter program")
window.minsize(width=500,height=300)
my_label = Label(text="hello bkl", font=("Arial",24,"bold"))
my_label.pack()
#my_label.pack() #its pack our label to show on screen. 
# my_label["text"] = "shivam"
# my_label.config(text="shivam tiwari")

#Button
# button = Button(text="Click Me")
# button.pack()

# def button_clicked():
#     print("I got clicked")

def call_label():
    new_text = input.get()
    my_label.config(text=new_text)
    

button = Button(text="click me ",command=call_label)
button.pack()

#Entry

input = Entry(width=10)
input.pack()






window.mainloop()


