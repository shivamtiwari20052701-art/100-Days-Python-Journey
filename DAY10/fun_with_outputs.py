# Add two parameters

def add_two_parameters(f_name,l_name):
    return f_name+l_name
# output=add_two_parameters("shivam","tiwari").title()


print(add_two_parameters("shivam","tiwari").title())

#to convert something in tittle case 
# e.g. SHIVAM--->Shivam , then use .tittle() fun at the end of the line we want print  


#Function have more than one output

def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
     return "no inputs given" 
    
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("what is your first name??"), input("what is your last name ??")))