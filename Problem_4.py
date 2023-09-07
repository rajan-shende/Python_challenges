# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

def calculate_area():
    radius = float(input("Enter radius of circle"))
    return round(3.14 * radius ** 2, 3)


print(calculate_area())