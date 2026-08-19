#File Not Found
# with open("a_file.txt") as file:
#     file.read()

#key Error 
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existant_key"]

#Index Error
# fruit_list = ["apple","banana","pear"]
# fruit = fruit_list[3]

#Type Error 
# text = "abc"
# print(text + 5)

# try:
#     file = open("DAY30//a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     file = open("DAY30//a_file.txt","w")
#     file.write("HEllo dosto")

# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("this is an error that i made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over three meters ")

bmi = weight/height**2
print(bmi)