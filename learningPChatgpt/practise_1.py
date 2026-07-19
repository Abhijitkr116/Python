# Write a program that:

# Asks the user for two numbers.
# Converts them to integers.
# Prints:
# Sum
# Difference
# Product
# Division
# Remainder
# Power (first number raised to the second)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum = a + b
difference = a-b
product = a*b
division = a/b
remainder = a%b
power = a**b

print(f"The sum of {a} and {b} is: {sum}")
print(f"The difference of {a} and {b} is: {difference}")
print(f"The product of {a} and {b} is: {product}")
print(f"The division of {a} and {b} is: {division}")
print(f"The remainder of {a} and {b} is: {remainder}")
print(f"The power of {a} and {b} is: {power}")
