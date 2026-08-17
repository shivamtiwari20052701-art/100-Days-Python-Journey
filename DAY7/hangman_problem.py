import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# todo- create a variable called lives to keep track of the number of lives left 
lives=6

word_list=["aardvark", "baboon", "camel"]
Choosen_word=random.choice(word_list) 
print(Choosen_word)
placeholder=""
for letter in Choosen_word:
    placeholder += "_"
print(placeholder)
game_over = False
correct_letter=[]
while not game_over:
    guess=input("guess a letter :").lower()
    display = " "
    # change the for loop so that you can keep the previous letters
    for letter in Choosen_word:
        if letter==guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter 
        else:
            display += "_"
           
    print(display)

    if guess != Choosen_word:
        lives -= 1
    if lives==0:
        game_over=True
        print("You Lost!!")
    print(stages[lives])

    if "_" not in display:
        game_over=True
        print("you won")
    
   
