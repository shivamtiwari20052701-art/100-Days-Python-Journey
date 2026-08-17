from menu_coffee import MENU, resources
from art import logo
print(logo)
start_machine=True
def check_ingredients(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def compare_amount(money,cost):
    if money>=cost:
        return True
    elif cost>money:
        return False
    
def calculate_amount(money,cost):
    if  money>cost:
        return money-cost
    elif money==cost:
        return 0 
def update_resources(ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
while start_machine:
    user_choice=input("What would you like? (espresso/latte/cappuccino):")
    if user_choice=="off":
        start_machine=False
    elif user_choice=="report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money: ₹{resources['money']}")
    elif user_choice in MENU:
        drink=MENU[user_choice]
        ingredients = drink["ingredients"]
        cost=drink["cost"]
        if check_ingredients(ingredients):
            print("Resources are sufficient")
            print("Insert the money")
            money=int(input("enter the money"))
            if compare_amount(money,cost):
                print("Payment successful!")
                return_change=calculate_amount(money,cost)
                update_resources(ingredients)
                if return_change>0:
                    print(f"here is: ₹{return_change} in change.")
                    
                elif return_change==0:
                    print("exact payment")
                resources["money"]+=cost
                print(f"Here is your {user_choice} ☕. Enjoy!")

            else:
                print("insufficient money")
    else:
        print("wrong input entered try again")
        

    

    


