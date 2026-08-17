import pandas

data = pandas.read_csv("DAY25/squirrel.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color": ["Gray","cinnamon","Black"],
    "count": [grey_squirrel,red_squirrel,black_squirrel]
}

DF = pandas.DataFrame(data_dict)
DF.to_csv("DAY25/squirrel_count.csv")
