bmi=84/1.65**2
print(bmi)
print(int(bmi))#flooring of number
print(round(bmi))#nearest number
print(round(bmi,2))# round off the number up to 2 digit

#Assignment operators
score=0
#when player scores a point
score+=1
print(score)
#and we can same do as -=,*=,/=

#f-strings
print("your score is:" + str(score))

height=1.5
is_winning=True 
print(f"your score is = {score}, your height is= {height}. your winning status is {is_winning}")