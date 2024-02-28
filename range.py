# Step 1: Ask the user to input a number
number = int(input("Enter a number for the multiplication table: "))

# Step 2: Ask the user to input the range
range_limit = int(input("Enter the range for the multiplication table: "))

# Step 3: Generate and display the multiplication table
print("Multiplication table for", number, "up to", range_limit, ":")
for i in range(1, range_limit + 1):
    print(number, "x", i, "=", number * i)
