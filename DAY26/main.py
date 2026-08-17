# numbers = [4,3,2,2]
# new_numbers = []

# for n in numbers:
#     add_1 = n+1
#     new_numbers.append(add_1)

# print(new_numbers)

#now same thing using list comprehension
# numbers = [4,3,2,2]

# new_items = [n+1 for n in numbers]
# print(new_items)

#with strings
# name = 'shivam'
# new_letters = [letter for letter in name]
# print(new_letters)#will split the name into letters 

#with range 
# range(1,5)

# new_range = [n*2 for n in range(1,5)]
# print(new_range)

#by giving some of the condition in List 
names = ["Aarav", "Vivaan", "Aditya", "Rohan", "Shivam", "Karan"]
# short_names = [n for n in names if len(n) < 6]
# print(short_names)
long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)
