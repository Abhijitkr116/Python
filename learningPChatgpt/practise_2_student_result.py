math = int(input("Enter marks for Math: "))
science = int(input("Enter marks for Science: "))
english = int(input("Enter marks for English: "))

total = math + science + english
average = total / 3

print(f"Total marks obtained: {total}")
print(f"Average marks: {average}")

print(f"Average marks are greater than 40: {average > 40}")
print(f"All three marks are greater than 35: {math > 35 and science > 35 and english > 35}")