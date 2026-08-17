#PYTHON DICTIONARY.
Programming_dictionary={"bug": "an error in program which prevents to running the program",
                        "function":"a piece of code that can be call agian and again",
                        }
#retrive the dictionary elements
print(Programming_dictionary["bug"])

#if want to add new entry 
Programming_dictionary["loop"]="a action of something that doing over and over again"
print(Programming_dictionary["loop"])

#to print the whole dictionary 
print(Programming_dictionary)

# wipe an existing dictionary 
# Programming_dictionary={}
# print(Programming_dictionary) #prints only {}

#edit an item in a dictionary 

Programming_dictionary["bug"]="error404"
print(Programming_dictionary["bug"])

#Loop through a dictionary
for items in Programming_dictionary:
    print(items)#prints the key 
    print(Programming_dictionary[items])#prints value of the key