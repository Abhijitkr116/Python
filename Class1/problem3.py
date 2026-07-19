import os

path = "/Riot Games/"

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)