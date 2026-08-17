# year=int(input("what is your date of birth??"))

# if year >= 1980 and year <= 1994:
#     print("you are a mellennial")
# elif year > 1994:
#     print("you are Gen Z.")

'''exception handling'''
try:
    age=int(input("how old are you?"))
except ValueError:
    print("you have typed wrong input please write correct input such as 15")
    age=int(input("how old are you?"))


if age>18:
    print(f"you can drive at age {age}")