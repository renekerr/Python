# Continue and Break statements

### This program prints every character of the string

for char in "computer":
    print(char)

print("Finished the for loop \n")


### This programs shows the use of continue statement in a for loop

for char in "computer":
    if char == "p": # if "p" is found then it is skipped and continue to next character
        continue
    print(char)

print("Finished the loop with a continue\n")


### This program shows the use of break statement in a for loop

for char in "computer":
    if char == "p": # if a "p" is found it breaks the for loop
        break
    print(char)

print("Finished the for loop with a break")






