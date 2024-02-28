# Step 1: Ask the user to input a number
num = int(input("Enter a number to check if it's prime: "))

# Step 2: Initialize a flag variable to track if the number is prime
is_prime = True

# Step 3: Check if the number is prime
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

# Step 4: Display the result
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
