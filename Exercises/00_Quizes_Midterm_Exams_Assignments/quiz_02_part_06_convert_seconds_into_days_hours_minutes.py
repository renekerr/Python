# Quiz 2 Part 6
# Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds,
# your program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly
# in the format specified below.

user_response = input("Enter a positive integer: ")
given_secs = int(user_response)


# Calculate the days
days = given_secs // 86400 # 1 day = 86400 seconds
seconds_1 = given_secs % 86400   # remaining seconds after we get days


# Calculate the hours
hours = seconds_1 // 3600 # 1 hour = 3600 seconds
seconds_2 = seconds_1 % 3600


# Calculate the minutes
minutes = seconds_2 // 60 # 1 minute = 60 seconds
seconds_3 = seconds_2 % 60 # remaining seconds


print(days, "days", hours, "hours", minutes, "minutes", seconds_3, "seconds")

