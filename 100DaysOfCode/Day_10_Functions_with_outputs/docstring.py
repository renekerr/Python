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
    

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])