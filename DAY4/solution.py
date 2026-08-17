#figure out to pick a name from the list of friends.
import random
friends=["shivam","kirtan","veer","krishna"]
#OPTION 1
# card_to_be_used=random.randint(0,3)
# if card_to_be_used==0:
#     print("shivam")
# elif card_to_be_used==1:
#     print("kirtan")
# elif card_to_be_used==2:
#     print("veer")
# else :
#     print("krishna")

#option 2 
# print(random.choice(friends)) #it makes the random choice from the given friends list   

#option 3
# random_index=random.randint(0,3)
# print(friends[random_index])#uses index to print 


#to find the length of list 
# print(len(friends))

#how to solve index error
num_of_friends=len(friends) #4->3
print(friends[num_of_friends-1])
