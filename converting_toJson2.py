import json

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Welcome to the Simple Math Calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = None
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    
    # Convert result to a dictionary
    result_dict = {"result": result}
    
    # Convert dictionary to JSON
    result_json = json.dumps(result_dict)
    
    print("Result in JSON format:", result_json)
else:
    print("Invalid input!")
