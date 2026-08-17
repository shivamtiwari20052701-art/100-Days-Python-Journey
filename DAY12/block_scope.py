#python do not have any block_scope!!

# game_level=3
# enemies=["skeleton","zobie","alien"]
# def create_enemy():
#     if game_level < 5:
#         new_enemy=enemies[0]
#     print(new_enemy)#this can be access but if what if we create it inside a function 
#IF we print new enemy outside the function??
# print(new_enemy)#gives error


#modification of global variablers
a=1
def increment_a():
    global a
    a+=1#we cant do this without global keyword
    print(f"increased a:{a}")
increment_a()
