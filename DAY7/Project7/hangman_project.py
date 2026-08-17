import random
from hangman_words import word_list
#1. update the wordlist to use the wordlist from the hangman_words.py
lives=6
#w. import the logo from hangman_logo.py 
from hangman_logo import logo,stages
print(logo)
Choosen_word=random.choice(word_list) 
print(Choosen_word)
place_holder=" "#for '_'
for letter in Choosen_word:
    place_holder +="_"
print(place_holder)

game_over = False#for while loop.
choosed_list=[]#to store already guessed values
already_guessed=" "

while not game_over:
    #tell user how many lives left
    print(f"---------------{lives}/6 Lives left-----------------------------")
    guess=input("Guess a letter!! \n").lower()

    #print the letter user has already guessed
    if guess in choosed_list:
        print(f"you have already guess:{guess}")
    
    display=" "#to display guess letter
    for letter in Choosen_word:
        if letter==guess:
            display +=letter
            choosed_list.append(guess)
        elif letter in choosed_list:
            display +=letter
        else:
            display +="_"
    print("word to guess :" + display)

    # if the letter is not in the choosen_word , print out the letter and let them know its not from the word
    #i.e. you guessed d, its not in the word. you lost a life.
    if guess not in Choosen_word:
        lives -= 1
        print(f"you guess: {guess}, it's not in the word. you lost a life.")
    if lives==0:
        game_over=True

        # tell user the correct word
        print(f"--------------the correct word was: {Choosen_word}\n you Lost!! ")

    if '_' not in display:
        game_over=True
        print("----------------you won!!-----------------")
    
    #print the stages
    print(stages[lives])
        