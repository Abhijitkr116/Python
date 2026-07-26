# Write a program to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up!

# words = {
#     "madad": "Help",
#     "khushi": "Happy",
#     "dukhi": "Sad",
#     "mushkil": "difficult or hard",
# }

# word = input("Enter the word you want the meaning of: ")

# print(words[word])



# Write a program to display all the eight numbers from the user and display all the unique numbers(once).

# s = set()

# n = input("Enter the 1 number: ")
# s.add(int(n))
# n = input("Enter the 2 number: ")
# s.add(int(n))
# n = input("Enter the 3 number: ")
# s.add(int(n))
# n = input("Enter the 4 number: ")
# s.add(int(n))
# n = input("Enter the 5 number: ")
# s.add(int(n))
# n = input("Enter the 6 number: ")
# s.add(int(n))
# n = input("Enter the 7 number: ")
# s.add(int(n))
# n = input("Enter the 8 number: ")
# s.add(int(n))

# print(s)



# Can we have a set with 18 (int) and '18' as (str) as a value in it?

# s = set()

# s.add(18)
# s.add('18')

# print(s)



# What will be the length of the following sets:

# s = set()

# s.add(20)
# s.add(20.0)
# s.add('20')

# print(s, len(s))


# What is the type of 's'?

# s = {}

# print(type(s))




# Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

# a = {}

# name = input("Enter your name: ")
# language = input("Enter your fav. language: ")
# a.update({name: language})

# name = input("Enter your name: ")
# language = input("Enter your fav. language: ")
# a.update({name: language})

# name = input("Enter your name: ")
# language = input("Enter your fav. language: ")
# a.update({name: language})

# name = input("Enter your name: ")
# language = input("Enter your fav. language: ")
# a.update({name: language})

# print(a)



# If the names of 2 friends are same, what will happen to the program in prev. problem?
# => It will update the value with the same name



# If the values of the 2 names are same, what will happen?
# => Values can be same in dict(), because we can identify dict using key values that is name in this case so values can be same but not the keys that are names.



# Can you change the value inside a list which is contained in a set s?

# s = {8, 7, 12, 'Harry', [1,2]}

# First of all we can't assign any list values into set
# Second indexing is not allowed in set, So we can't change any value

