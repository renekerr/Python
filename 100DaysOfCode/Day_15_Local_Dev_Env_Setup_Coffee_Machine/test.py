def resources_update(water_used, milk_used, coffee_used):
    resources['water'] -= water_used
    resources['milk'] -= milk_used
    resources['coffee'] -= coffee_used
    return resources['water'], resources['milk'], resources['coffee']


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(resources)

w, m, c = resources_update(water_used=150, milk_used=100, coffee_used=25)
print(w)
print(m)
print(c)









