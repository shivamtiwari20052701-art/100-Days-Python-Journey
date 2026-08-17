import random
names = ["Aarav", "Vivaan", "Aditya", "Rohan", "Shivam", "Karan"]
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

#creating new dictionary using a existing dict. using conditions
#new_dict{new_key:new_value for (key,value) in dict.items() if test}
# dict = {'Aarav': 3, 'Vivaan': 13, 'Aditya': 82, 'Rohan': 95, 'Shivam': 90, 'Karan': 65}
# passed_students ={students:score for (students,score) in dict.items() if score >60}
# print(passed_students)

Student_dict = {
    "student" :["Aarav", "Vivaan", "Aditya", "Rohan", "Shivam", "Karan"],
    "score" : [45,34,76,54,94,56]
}

import pandas
student_data_frame = pandas.DataFrame(Student_dict)
#print(student_data_frame)
#looping through the data frame 
# for (key,value) in student_data_frame.items():
#     print(value)


#Loop through rows of a data frame

for (index,row) in student_data_frame.iterrows():
    #print(row)
    #print(index)
    if row.student == "Shivam":
        print(row.score)