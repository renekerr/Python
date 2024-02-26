# Fill an empty dictionary
user_info = {}

stop_add = False

while not stop_add:
    user_name = input('User name: ')
    user_age = int(input('Age: '))

    user_info[user_name] = user_age

    continue_adding = input("Add more users, 'yes' or 'no'. ")
    if continue_adding == 'no':
        stop_add = True
        print()....





