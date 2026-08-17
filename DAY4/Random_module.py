import random #includes everything in random module
# import my_module#thats how we can create our own random module 
# random_integer=random.randint(1,10)
# print(random_integer)
# # print(my_module.my_fav_number) thats how we used owr own module

#how to create a floating point random number 
# random_number_0_to_1=random.random ()*10 
# #here first random stands for random module and second random stands for random function which do not take any of the arguments.---here is zero is inclusive but 10 is not inclusive.
# print(random_number_0_to_1)

# #RANDOM FLOAT
# random_float=random.uniform(1,10)
# print(random_float)

#print heads or tails
random_flip=random.randint(0,1)
if random_flip==0:
    print("Heads")
else:
    print("Tails")
    