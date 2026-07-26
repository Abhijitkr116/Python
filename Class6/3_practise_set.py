# Input 4 numbers from the user and find the greatest number

# a1 = int(input("Enter the number: "));
# a2 = int(input("Enter the number: "));
# a3 = int(input("Enter the number: "));
# a4 = int(input("Enter the number: "));

# if(a1>a2 and a1>a3 and a1>a4):
#     print(f"The largest number is a1, {a1}")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print(f"The largest number is a2, {a2}")
# elif(a3>a1 and a3>a2 and a3>a4):
#     print(f"The largest number is a3, {a3}")
# elif(a4>a1 and a4>a2 and a4>a3):
#     print(f"The largest number is a4, {a4}")



# Write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# Maths = int(input("Enter your Maths marks: "))
# Science = int(input("Enter your Science marks: "))
# English = int(input("Enter your English marks: "))

# total_percentage = (100*(Maths + Science + English) / 300)

# if(Maths >= 33 and Science >= 33 and English >= 33 and total_percentage > 40):
#     print(f"Congratulations you're passed, {total_percentage}%")
# else:
#     print(f"Better luck next time, you got only: {total_percentage}%")



# A spam comment is defined as a text containing following keywords: 
#     "Make a lot of money", "Buy now", "Subscribe this", "Click this"
#         Write a program to detect these spams

# first way
# keywords = input("Enter the message: ")

# if(keywords == "Make a lot of money" or keywords == "Buy now" or keywords == "Subscribe this" or keywords == "Click this"):
#     print("This is a spam mail, don't click on it")
# else:
#     print("Safe mail, Go ahead!")


# second way
# p1 = "Make a lot of money"
# p2 = "Buy now"
# p3 = "Subscribe this"
# p4 = "Click this"

# message = input("Enter your comment: ")

# if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
#     print("this is a spam mail, ignore it...")
# else:
#     print("This is not a spam mail")



# Check whether the username length is greater 10 or not

# username = input("Enter your username: ")

# if(len(username)>10):
#     print("The length is greater than 10")
# else: 
#     print("The length is less than 10, please enter the username again")



# Write a program which finds out whether a given name is present in list or not

# names = ["Abhijit", "Aman", "Sunaina", "Abhishek", "Sujeet"]

# name = input("Enter the name: ")

# if(name in names):
#     print(f"This name is matching, {name}")
# else:
#     print(f"This name is not matching, {name}")



