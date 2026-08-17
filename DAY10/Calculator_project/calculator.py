from logo import logo
print(logo)


"""this function going to perform the addition operation"""
def add(n1,n2):
    return n1+n2
"""this function going to perform the subtraction operation"""
def sub(n1,n2):
    return n1-n2
"""this function going to perform the multiplication operation"""
def mul(n1,n2):
    return n1*n2
"""this function going to perform the divide operation"""
def div(n1,n2):
    if n2<=0:
        return f"division is not possible"
    else:
        return n1/n2
    


"""make a dictionary and make 4 fn as value and operations as value"""

operations ={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
    

    }

 
def calculator():
    should_accumulate=True 

    """ask the user for first number """

    n1=float(input("enter your first number :"))


    while should_accumulate :
        """ask the user for operation"""
        for symbol in operations:
            print(symbol)

        operation_symbol=input("enter your choice:")

        """ask the second number """
        n2=float(input("enter your number to process further:"))

        answer=operations[operation_symbol](n1,n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice=input("enter y to continue calculating and n to stop")
        print(choice)

        if choice=="y":
            n1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()
calculator()


        
        

            

        
        

        