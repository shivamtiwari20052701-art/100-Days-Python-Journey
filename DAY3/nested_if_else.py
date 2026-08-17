 #Nested if /else
print("welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))
if height>=120:
    print("You can ride the rollercoaster. ")
    age=int(input("enter age for the price per person"))
    if age<12:
        print("you have to pay $5")
    elif age<18:
         print("you have to pay $7")
    else :
        print("you have to pay $12")

else:
    print("sorry you have to grow talller before you can ride. ")