#list is a data structure which stores data and accepts all data types together
# e.g fruits=[item1,item2,....,....]

states_of_India = ["rajasthan","madhyapradesh","uttarpradesh","bihar"]
#To change data inside the list
states_of_India[0]="Raj."
#we can also add items in our list by using append() , function
states_of_India.append(["jharkhand"])
states_of_India.extend(["",""])#add bunch of list 
print(states_of_India[0])
print(states_of_India[1])
print(states_of_India[2])
print(states_of_India[3])

