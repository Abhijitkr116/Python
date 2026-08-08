'''
Rescursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller, similar subproblems.

factorial(1) = 1 
factorial(2) = 1 x 2 
factorial(3) = 1 x 2 x 3
factorial(4) = 1 x 2 x 3 x 4
factorial(5) = 1 x 2 x 3 x 4 x 5

factorial(n) = n x factoial(n-1)
'''

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number to calculate its factorial: "))

print(f"The factorial of {n} is: {factorial(n)}")