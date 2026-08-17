#sum function:-it adds the all values inside the list i.e

student_scores = [123,433,456,765,235,765,788,778,987,356]
total_score = sum(student_scores)
print(total_score)

#we can also perform this using for loop
sum = 0
for score in student_scores:
    sum += score
print(sum)

#maximum number-->
print(max(student_scores))     

# next method 
max_score=0
for score in student_scores:
 if score > max_score:
    max_score=score
print(max_score)