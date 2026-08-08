# Write a program using functions to find the greatest of three numbers

# def greatest(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     return c

# print(greatest(3,24,3))



# Write a python program using function to convert Farenheit to Celsius.

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F: "))

# c = f_to_c(f)
# print(f"The {f} Farenheit is converted to {round(c,2)}°Celcius")



# How do you prevent a python print() to print a new line at the end

# print("Abhijit", end="")
# print("Aman")
# print("Aarif")
# print("Abhishek")



# Write a recursive function to calculate the sum of first n natural numbers

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + n-1 + n
sum(n) = sum(n-1) + n
'''

# def sum(n):
#     if n == 1:
#         return 1
#     return sum(n-1) + n

# print(sum(5))





# Write a python function to print first n lines of the following pattern: 

'''
* * *
* *
*
'''

# def pattern(n):
#     if n==0:
#         return
#     print("* " * n)
#     pattern(n-1)

# pattern(3)





# Print a table using recursion 

# def table(n, i=1):
#     if i==11:
#         return 0
#     print(f"{n} x {i} = {n*i}")
#     table(n, i+1)

# table(5)





# Write a python program which convert inches to cms

# def inch_to_cms(inch):
#     return inch * 2.54

# print(round(inch_to_cms(6.2),2))





# Fucking code

# # Write a python function to remove a given word from a list and strip at the same time. 

# def strip(l, word):
#     n = []
#     for i in l:
#         if i != word:
#             n.append(i.strip(word))
#     return n

# l = ["Rohan", "Vishal ", "Simran", "Aman"]

# print(strip(l, "Aman"))





