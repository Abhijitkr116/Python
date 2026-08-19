import random
# Write a program to read the text from the given file 'poem.txt' and find out the whether it contains the word "twinkle" or not 

# word = "Twinkle"

# f = open("poem.txt")
# content = f.read() // Use it 

# with open("poem.txt") as d: // Or use it
#     content = d.read()
#     if("Twinkle" in content):
#         print("Twinkle word is present")
#     else:
#         print("Twinkle word is not present")

# f.close()





# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update a Hi-score whenever game() function breaks the Hi-score.

# def game():
#     print("You are playing the game...")
#     score = random.randint(1, 62)
#     #Fetch the hi-score
#     with open("hi-score.txt") as f:
#         hiscore = f.read()
#         if hiscore != "":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score is {score}")
#     print(f"Your hi-score is {hiscore}")

#     if(score>hiscore):
#         #store the hiscore to the file
#         with open("hi-score.txt", "w") as f:
#             f.write(str(score))
            
#     return score

# game()





# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a - 13 year old

# def generate_tables(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2, 21):
#     generate_tables(i)





# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file

# word = "donkey"

# with open("donkey.txt", "r") as f:
#     content = f.read()

#     new_content = content.replace("donkey", "riddhi")

# with open("donkey.txt", "w") as d:
#     d.write(new_content)





# Repeat the previous program for a list of such words to be censored

# words = ["donkey", "gadha", "bad"]

# with open("donkey.txt", "r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#"*len(word))

# with open("donkey.txt", "w") as d:
#     d.write(content)





# Write a program to mine a log file and find out whether it contains 'python'

# with open("log.txt", "r") as f:
#     content = f.read()

#     if ("python" in content):
#         print("Yes, python is present")
#     else:
#         print("No, python is not present")





# Write a program to find out the line number where the python is present

# with open('log.txt', "r") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"Yes python is present in line no: {lineno}")
#         break
#     lineno += 1
# else:
#     print("'Python' is not present...")





# Write a program to make a copy of text file "this.txt" 

# with open("this.txt", "r") as f:
#     content = f.read()

# with open("this_copy.txt", "w") as f:
#     f.write(content)





# Write a program to find out whether a file is identical and matches the content of another file 

# with open("this.txt") as f:
#     content1 = f.read()

# with open("this_copy.txt") as f:
#     content2 = f.read()

# if content1 == content2:
#     print("Yes these files are identical...")
# else:
#     print("No these files are not identical...")





# Write a program to wipe out the content of a file using python

# with open("this_copy.txt", "w") as f:
#     f.write("")





# Write a python program to rename a file to "rename_by_python.txt"

# steps: Just copy the same data of another file
#        and create with new renamed file name
#        and delete the old data by using some inbuilt functions