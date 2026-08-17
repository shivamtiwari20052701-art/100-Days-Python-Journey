from tkinter import *

def temp_button():
    print("I got clicked ")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My gui code")
window.minsize(height=500, width=300)
#to add padding(extra space between borders and text)
window.config(padx=20,pady=20)


#Label

my_label = Label(text="I am label ",font=('Arial',24,'bold'))
my_label.config(text="New text")
#my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)
my_label.pack

#button

button = Button(text="Click me " , command=temp_button)
button.grid(row=1,column=1)


#new button
new_button = Button(text="daba na laude",command=temp_button)
new_button.grid(row=0,column=2)


#Entry

input = Entry(width=10)
print(input.get())
input.grid(row=3,column=3)




window.mainloop()
