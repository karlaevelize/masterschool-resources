def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Would you like to add, subtract, multiply, or divide?")
    operation = input()
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        result = "Invalid operation"
    
    print(f"The result is: {result}")
