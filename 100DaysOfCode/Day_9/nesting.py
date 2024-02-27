# Nesting dictionaries and lists
# Given this dictionary
capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

# Add/edit an item to a dictionary
capitals["Spain"] = "Madrid"
capitals["Spain"] = "Barcelona" 

# Retrieving key-value pairs in a dictionary
for key in capitals:
    print(key, capitals[key])


#**** Nesting a list in a dictionary ****
travel_log ={
    "France": ["Paris", "Lyon", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Add/edit item to a list inside a dictionary
travel_log["Spain"] = ["Madrid", "Barcelona", "Valencia"]
travel_log["Spain"][2]= "Sevilla"

# Retriving key-value items
for k, elem in enumerate(travel_log.values()):
    print(k, elem)


#*** Nesting a dictionary in a dictionary ****
travel_log = {
    "France":{"cities_visited":["Paris", "Lyon", "Dijon"], "total_visits" :10},
    "Spain": {"cities_visited":["Madrid", "Barcelona", "valencia"], "total_visits" :6},
}

# Add/edit items
travel_log["Netherland"] = {"cities_visited": ["Amsterdam", "Rotterdam", "Utrecht"], "total_visits": 3}
travel_log["Netherland"] = {"total_visits": 2}


#**** Nesting dictionaries in lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lyon"],
        "total_visits" : 3
    },
    {
        "country": "Spain",
        "cities_visited": ["barcelona", "Madrid"],
        "total_visits" : 5
    }
]

# Add/edit item in dictionary in a list
travel_log.append({
        "country": "New Zealand",
        "cities_visited": ["Auckland", "Rotorua"],
        "total_visits" : 2
})

travel_log[2]["cities_visited"].append('Christchurch')
travel_log[0]["cities_visited"].append('Marseille')

print(travel_log)