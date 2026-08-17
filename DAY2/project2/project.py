#project2:-tip calculator
print("Welcome to tip calculator!")
bill=float(input("what was the total bill?"))
tip=int(input("How much tip you want to give ? 10 , 12 or 15 ?"))
people=int(input("how many peoples to split the bill?"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=total_tip_amount+bill
each_person=total_bill/people
final_amount=(round(each_person,2))
print(f"Each person have to pay: ${final_amount}")

