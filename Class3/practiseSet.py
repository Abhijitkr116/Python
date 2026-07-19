# name = input("Enter your name : ")

# print(f"Good Night, {name}")

# Start it from 1:42:56

# letter = '''Dear <|NAME|>,
# You are selected!
# Date: <|DATE|>'''

# letter = letter.replace("<|NAME|>", "Abhijit").replace("<|DATE|>", "7/13/2026")

# print(letter)

# Write a program to detect double spaces in a string.

string = "This is a string with double  spaces."

print(string.find("  "))  # This will return the index of the first occurrence of double spaces, or -1 if not found.

#Replace double spaces with single space

string = string.replace("  ", " ")
print(string)