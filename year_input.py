# Step 1: Ask the user to input a year
year = int(input("Enter a year to check if it's a leap year: "))

# Step 2: Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
