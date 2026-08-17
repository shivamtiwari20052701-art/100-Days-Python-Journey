import random
letters=["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['!', '#', '$', '%', '&', '*' , '(' , ')'] 

print("Welcome to passward generator!!")
nr_letters=int(input("how many letters do you want in your password??\n"))
nr_numbers=int(input("how many numbers would you like??\n"))
nr_symbols=int(input("how many symbols you like??\n "))

#easy level 

# password= " "

# #for letters
# for char in range(0,nr_letters):
#     password +=random.choice(letters)

# #for numbers
# for char in range(0,nr_numbers):
#     password += random.choice(numbers)

# #for symbols
# for char in range(0,nr_symbols):
#     password +=random.choice(symbols)

# print(password)

#hard level 

password_list= []

#for letters
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

#for numbers
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

#for symbols
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

#suffles the passward 
random.shuffle(password_list)


password=" "
for char in password_list:
    password += char

print(f" Your password is : {password}")






