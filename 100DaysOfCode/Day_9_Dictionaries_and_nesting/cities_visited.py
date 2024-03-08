'''
LESSON 23 DAY 9 - DICTIONARY IN LIST
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

Example Input
Brazil
5
["Sao Paulo", "Rio de Janeiro"]
Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo.

'''

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.

# Option I - Append items right away
def add_new_country(country, visits, list_of_cities):
    """
    Adds a new country entry to the travel log data structure.
  
    Args:
        country (str): The name of the country.
        visits (int): The number of times the user has visited the country.
        list_of_cities (list): A list containing the names of cities visited in the country.
  
    Returns:
        None
  
    Appends a dictionary containing the provided information about the country to the `travel_log` variable, which is assumed to be a list. This dictionary uses the keys"country",    "visits", and "cities" to store the corresponding information.
    """
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities" : list_of_cities
})
    


# Option II - Create an empty dict and add items then append it
def add_new_country_ii(country_name, number_visits, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)


# Do not change the code below 👇
add_new_country_ii(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")