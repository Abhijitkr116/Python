age = int(input("Enter your age: "));

if age >= 18:
    print("You can vote...")
elif age <= 0: 
    print("Check the number again and write the correct value...")
else:
    print("You're below the age of 18")