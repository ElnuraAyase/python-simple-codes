def fibonacci(n): 
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)
        def fibonacci(n):

result =  [fibonacci(i) for i in range(10)]
print(result)  
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

