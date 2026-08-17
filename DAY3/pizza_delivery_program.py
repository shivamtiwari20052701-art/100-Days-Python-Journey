print("Welcome to python pizza deliveries!")
size=input("what size of pizza do you want? S, M OR L:")
pepperoni=input("do you want pepperoni on your pizza? Y or N:")
extra_cheese=input("do you want extra cheese? Y or N:")
price=0
if size=="S":
    price=15
    print("Price of small pizza is : $15")
    if pepperoni=="Y":
        price+=2
        print(print(f"price after adding papperoni is:{price}"))
        if extra_cheese=="Y":
         price+=1
        print(f"price after adding extra cheese is:{price}")
elif size=="M":
    price=20
    print("price of medium pizza is: $20 ")
    if pepperoni=="Y":
        price+=3
        print(print(f"price after adding papperoni is:{price}"))
        if extra_cheese=="Y":
         price+=1
        print(f"price after adding extra cheese is:{price}")
else:
    price=25
    print("price of large pizza is : $25")
    if pepperoni=="Y":
        price+=3
        print(f"price after adding papperoni is:{price}")
        if extra_cheese=="Y":
         price+=1
        print(f"price after adding extra cheese is:{price}")
