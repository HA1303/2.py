print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

first_input = input("Enter your first number: ")
second_input = input("Enter your second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    result = add(first_number, second_number)
    print(f"Result: {result}")
elif operation == "subtract":
    result = subtract(first_number, second_number)
    print(f"Result: {result}")
elif operation == "multiply":
    result = multiply(first_number, second_number)
    print(f"Result: {result}")
elif operation == "divide":
    result = divide(first_number, second_number)
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")