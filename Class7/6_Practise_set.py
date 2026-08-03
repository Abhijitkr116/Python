# Write a python program to print multiplication table of a given number using for loop

# n = int(input("Enter a number to print its multiplication table: "))

# for i in range (1,11):
#     print(f"{n} x {i} = {n*i}")



# Write a program to greet names stored in a list 'l' and which starts with S

# l = ["Harry", "Sohan", "Sachin", "Rahul", "Sonam"]

# for i in l: 
#     if(i.startswith("S")):
#         print("Hello " + i)




# Attempt problem 1 using while loop

# num = int(input("Enter a number to print its multiplication table: "))

# i = 1

# while(i<=10):
#     print(f"{num} x {i} = {num*i}")
#     i += 1;




# Write a program to find whether a given number is prime or not

# n = int(input("Enter a number to check if it is prime or not: "))

# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is not a prime number.")
#         break
# else:
#     print(f"{n} is a prime number.")



# Write a program to find the sum of first natural numbers using while loop

# n = int(input("Enter a number to find the sum of first natural numbers: "))

# i = 0
# sum = 0

# while(i<=n): 
#     sum += i
#     i += 1

# print(f"The sum of first {n} natural numbers is: {sum}")



# write a program to calculate the factorial of a given number using for loop

# n = int(input("Enter a number to calculate its factorial: "))

# sum = 1

# for i in range (1, n + 1):
#     sum *= i

# print(f"The factorial of {n} is: {sum}") 


'''
Write a program ot print following star pattern

n=3

   *
  ***
 *****

'''

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("\n")



'''
Write a program ot print following star pattern

n=3

*
**
***
'''

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print("*" * i, end="")
#     print("\n")



'''
Write a program ot print following star pattern

n = 3

***
* * 
***
'''

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if (i == 1) or (i == n):
#         print("*" * n, end="")
#     else:
#         print(f"*{' ' * (n-2)}*", end="")
#     print("")



# Write a program to print multiplication table of a given number in reverse

# n = int(input("Enter a number to print its multiplication table: "))

# for i in range(1, 11):
#     print(f"{n} x {11-i} = {n*(11-i)}")