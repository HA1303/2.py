# main.py
import calculator

print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")

first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    result = calculator.add(first_number, second_number)
    print(f"Result: {result}")
elif operation == "subtract":
    result = calculator.subtract(first_number, second_number)
    print(f"Result: {result}")
elif operation == "multiply":
    result = calculator.multiply(first_number, second_number)
    print(f"Result: {result}")
elif operation == "divide":
    result = calculator.divide(first_number, second_number)
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")