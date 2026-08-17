capitals={
    "Rajasthan": "Jaipur",
    "MP": "Bhopal",
    "UP":"Lucknow",
    "Bihar": "Patna"

}

#nested list in Dictionary

travel_log={
    "Rajasthan": ["Jaipur","Kota","SWM","Tonk"],
    "MP": ["Rewa","Jabalpur","Sidhi","Satna"],
    "UP": ["Pryagraj","Agra","Sonbhadra"],
    "Bihar":["Aara","Buxar","Muzaffarpur"]
}

#print kota 
print(travel_log["Rajasthan"][1])

#Nested List

Nested_List=['a','b',['c','d']]

#print d from this nested list
print(Nested_List[2][1])

#Nested_Dictionary

travel_log = {
    "Rajasthan": {"num_times_visited": 14,
                  "cities_visited": ["Jaipur","Kota","SWM","Tonk"]
                  },
    "MP":{"num_times_visited":9,
        "cities_visited":["Rewa","Jabalpur","Sidhi","Satna"]
        },
    "UP":{"num_times_visited": 7,
    "cities_visited":["Pryagraj","Agra","Sonbhadra"]
        },
    "Bihar":{"num_times_visited": 13,
             "cities_visited":["Aara","Buxar","Muzaffarpur"]
             
}
}

#Print Buxar
print(travel_log["Bihar"]["cities_visited"][1])