from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card ={}#we made this global so that we can use it both of the functions
to_learn = {}

try:
    data = pd.read_csv("DAY31//data//words_to_learn.csv")#always opens the file where we have left(already learn words not included)
except FileNotFoundError:
    original_data = pd.read_csv("DAY31//data//french_words.csv")#for the initial run when user dont know anything
    all_words = original_data.to_dict(orient="records")
else:
    all_words = data.to_dict(orient="records")
def next_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)#stops the front screen untill we are clicking for the next word
    current_card = random.choice(all_words) 
    canvas.itemconfig(canvas_image, image=front_image)#next word aate hi front image show hoga  
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    flip_timer = window.after(3000,func=flip_card)
#------------------------------------------------flip the card------------------------------------------
def flip_card():
    #now change the image
    canvas.itemconfig(canvas_image,image=back_image)#card flip hote hi back image show hogi
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")

#---------------------------------Remove the known words----------------------------------------------------
def is_known():
    all_words.remove(current_card)#romoves the known words
    next_word()
    data = pd.DataFrame(all_words)
    data.to_csv("DAY31/data/words_to_learn.csv", index=False)#stores the data of remaining csv

    






#------------------------------------------User interface(UI)-----------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)
#waits for three seconds
flip_timer= window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526,)
back_image = PhotoImage(file="DAY31//images//card_back.png")
front_image = PhotoImage(file="DAY31//images//card_front.png")
canvas_image = canvas.create_image(400, 263,image=front_image)
card_title = canvas.create_text(400,150,text="Title", font=("Arial",30,"italic"))
card_word = canvas.create_text(400,263,text="Word", font=("Arial",40,"bold"))#word_text will be modified after click the cross
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

#cross buttton
cross_image = PhotoImage(file="DAY31//images//wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,borderwidth=0, command=next_word)
unknown_button.grid(row=1,column=0,padx=20,pady=20)

#right buttton
check_image = PhotoImage(file="DAY31//images//right.png")
known_button = Button(image=check_image, highlightthickness=0,borderwidth=0 , command=is_known)
known_button.grid(row=1,column=1,padx=20,pady=20)

next_word() #will change the text for the first time when we run the code








window.mainloop()


