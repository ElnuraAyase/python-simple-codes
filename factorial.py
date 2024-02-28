# Step 1: Ask the user to input a number
num = int(input("Enter a number to calculate its factorial: "))

# Step 2: Initialize the factorial variable to 1
factorial = 1

# Step 3: Calculate the factorial using a loop
for i in range(1, num + 1):
    factorial *= i

# Step 4: Display the factorial
print("The factorial of", num, "is:", factorial)
