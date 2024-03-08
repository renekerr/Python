# List Slicing Exercise 3 (Every Other Element)
# Write a function that accepts a list as input and returns a new list which includes every other element
# in the original list. Keep the first element, i.e. input_list[0].


def list_every_other_element(input_list):               # Define function
    output_list = []                                    # Assign variable as empty list
    list_lenght = len(input_list)                       # Calculate list's length

    output_list.append(input_list[0])                   # Keep the first element

    for index in range(1,list_lenght):                  # Loop from 1 to list's length (it will skip first element. index 0)

        if index % 2 == 0:                              # If index % 2 == 0
            output_list.append(input_list[index])       # Then append it to the list
    return output_list                                  # Return value(s)

# Main program
input_list = ["we", "love", "python", "so","much"]
f = list_every_other_element(input_list)

print(f)









