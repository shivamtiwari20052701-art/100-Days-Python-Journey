#Multiple if 
print("welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))
bill=0
if height>=120:
    print("You can ride the rollercoaster. ")
    age=int(input("enter age for the price per person"))
    if age<12:
        bill=5
        print("Child tickets are $5")
    elif age<18:
         bill=7
         print("Youth tickets are  $7")
    else :
        bill=12
        print("Adult tickets are $12")
        
        wants_photo=input("do you want to have a photo take ? type y for yes and n for no")
        if wants_photo=="y":
            bill +=3
            print(f"your total bill is: ${bill}")

else:
    print("sorry you have to grow talller before you can ride. ")