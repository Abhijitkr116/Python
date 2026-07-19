Empty = {}  # Empty dictionary

marks = {
    "Harry": 100,
    "Subham": 98,
    "Abhijit": 99,
    "Aman": 80
}

# print(marks.items()) # Returns the data with key in the form of tuple

# print(marks.keys()) # Returns the key data in the form of list

# print(marks.values()) # Return the values in the form of list

# marks.update({"Harry": 99}) # Can update the previous values
# marks.update({"Renuka": 100}) # Can add up the new values

# print(marks)

# print(marks.get("Harry"))
# print(marks["Harry"])

print(marks.get("Harry2"))  # Print None if any error occurs
print(marks["Harry2"])   # Will give error if any error occurs
