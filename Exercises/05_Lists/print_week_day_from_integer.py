# This program ask the user for a positive integer between 1 and 7 (both inclusive)
# And prints the corresponding day of the week in capital letters
# Assume that the day of the week starts from MONDAY


user_response = input("Please enter a number between 1 and 7 (both incl): ")
index = int(user_response)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[index - 1])
