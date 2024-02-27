# Testing for loop
x_count = 0
y_count = 0
z_count = 0

for x in range(1, 3):
    x_count = x_count + 1
    for y in range(1, 3):
        y_count = y_count + 1
        for z in range(1,3):
            z_count = z_count + 1
            print("x=", x, "", "y=", y, "z=", z)
print("")
print(x_count, "", y_count, "", z_count)

