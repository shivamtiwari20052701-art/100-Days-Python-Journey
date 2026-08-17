print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************
''')
print("Welcome to the treasure Island!")
print("Your mission is to find the treasure. ")
choice1=input("You're at a cross road. Where do you want to go?\n Type 'Left' or 'Right'")
if choice1=="Left":
    choice2=input("You have come to a lake. there is an island in the middle of the lake.\n Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if choice2=="wait":
        choice3=input("you have three doors: Red, yellow and blue.\n type 'red' to open red door ,'blue' for blue door and 'yello' for yellow door  ")
        if choice3=="red":
            print("Burned by fire!!\n Game Over!! ")
        elif choice3=="yellow":
            print("You won :)")
        elif choice3=="blue":
            print("Eaten by beasts.\n Game Over.")
        else:
            print("Game Over")
    elif choice2=="swim":
        print("Attacked by trout.\n Game over.")
    else :
        print("Game over")
elif choice1=="Right":
    print("Fall into a hole.\n Game Over!!")
else:
    print("Game over")






    
  