# You can set any default value to a function argument. If the user does not provide a value for that argument, the default value will be used.

def Greet(name, ending = "Thank you for visiting!"):
    print("Hello, " + name + "!")
    print(ending)
    return "Greeting sent successfully."

val = Greet("Abhijit");
print(val)