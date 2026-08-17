import random
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

print(logo)

#functions to check users guess against actual answeer. 
def check_number(guess, answer, turns):
    """checks answer against guess, returns the number of guess remaining"""
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:  
        print("too low")
        return turns-1
    else:
        print(f"you got it! the actual answer was {answer}")

#function to check the difficulty.
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard' ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

    
    

print("Welcome to number guessing game !!")
def game():
    #choosing a number between 1 and 100
    print("I am guessing a number between 1 and 100.")
    answer=random.randint(1,100)
    print(f"Psst , the correct answer is {answer}")

    turns=set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts to guess the number.")
        #functions to check users guess against  actual answer
        guess=int(input("make a guess"))
        turns=check_number(guess, answer,turns)
        if turns==0:
            print("you have run out of guesses, you lose.")
            return
        elif guess!=answer:
            print("guess again")
 
game()

 

