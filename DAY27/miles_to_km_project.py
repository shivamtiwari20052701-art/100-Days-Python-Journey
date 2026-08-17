from tkinter import *
def button_click():
    print("button is clicked")
    new_text = int(input.get())*1.6
    second_label.config(text=new_text)
#window screen 
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500,height=500)
window.config(padx=20,pady=20)
#label 1
first_label = Label(text="is equal to ",font=('Arial',24,'bold'))
first_label.grid(row=1,column=0)
#first_label.config(padx=2,pady=2)

#entry
input = Entry(width=10)
print(input.get())
input.grid(row=0,column=1)
#input.config(padx=2,pady=2)

#label 2
second_label = Label(text= "0" ,font=('Arial',24,'bold'))
second_label.grid(row=1,column=1)
#second_label.config(padx=2,pady=2)

#button 
button = Button(text="Calculate", command=button_click)
button.grid(row=2,column=1)
#button.config(padx=2,pady=2)

#label 3
third_label = Label(text= "Miles" ,font=('Arial',24,'bold'))
third_label.grid(row=0,column=2)
#third_label.config(padx=2,pady=2)

#label 4
fourth_label = Label(text= "Km" ,font=('Arial',24,'bold'))
fourth_label.grid(row=1,column=2)
#fourth_label.config(padx=2,pady=2)
window.mainloop()
