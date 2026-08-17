#Stone paper scissors project
import random 
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper='''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images=[rock,paper,scissors]

choice=int(input("what do you choose ?  Type 0 for rock, type 1 for paper , and type 2 for scissors \n "))
if choice>=0 or choice<=2:
    print(game_images[choice])
else:
    print("wrong choice selected ")
    exit()

choice1 = random.randint(0,2)
print("computer choice: \n")
print(game_images[choice1])

if choice==0 and choice1==1:
    print("you lost!!")
elif choice==0 and choice1==0:
    print("tied")
elif choice==1 and choice1==1:
    print("tied")
elif choice==2 and choice1==2:
    print("tied")
elif choice==1 and choice1==2:
    print("you lost ") 
elif choice==2 and choice1==0:
    print("you lost")
else:
    print("you won!!")

     
