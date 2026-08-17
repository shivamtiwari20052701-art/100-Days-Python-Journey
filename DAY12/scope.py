# enemies=1
# def increase_enemies():
#     enemies=2
#     print(f"enemies inside the function is {enemies}")
# increase_enemies()
# print(f"enemies outside the function is {enemies}") 


#Local scope
# def drink_potion():
#     potion_strength=2
#     print(potion_strength)
# drink_potion()

'''variables decleared within the fun. is only access inside the scope of that function '''
#it givees an error 
# print(potion_strength)


#Global scope

player_health=10

def drink_potion():
    potion_strength=2
    print(player_health)
drink_potion()

