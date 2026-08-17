# with open("DAY25/weather_data.csv") as csv_file:
#     weather_data= csv_file.readlines()
#     print(weather_data)------------here there are lots of commas so its hard to extract the data and needs lots of cleaning

# import csv

# with open("DAY25/weather_data.csv") as csv_file:
#     weather_data= csv.reader(csv_file)
#     temperature = []
#     # print(weather_data)---this will create object
#     for row in weather_data:
#         #print(row)#will print all the data 
        
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)



#pandas

import pandas
data = pandas.read_csv("DAY25/weather_data.csv")
#print(data)#gives output in very systematic way 
#print(data["temp"])

#data to dictionary convert

# data_dict = data.to_dict()
# print(data_dict)

#series to list converstion

#temp_list = data["temp"].to_list()
# print(temp_list)


#average of list

#print(sum(temp_list)/len(temp_list))


#average using pandas(series)
#print(data["temp"].mean())

#print(data["temp"].max())

#get data in columns 
#print(data["condition"])
#print(data.condition)

#get data in row 
#print(data[data.day=="Monday"])

#print the max. temp data in row

#print(data[data.temp == data.temp.max()])

#onday = data[data.day=="Monday"]
# print(Monday.condition)/

# Monday_temp = Monday.temp[0]
# monday_temp_f = Monday_temp * 9/5 + 32
# print(monday_temp_f)

#create dataframes from scratch

# data_dict = {
#     "name": ["Shivam","veer","kirtan"],
#     "age": [21,20,20]
# }

# data = pandas.DataFrame(data_dict)
# #print(data)
# data.to_csv("new_data.csv")