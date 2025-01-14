# Functions

# 1. Variables & Data Types Review

my_name = "Karla"
age = 29
score = 4.75
has_pets = "yes" # snake_case

# 2. Defining & Calling a Function

def say_hello():
    print("Hello")

def say_hi():
    print("Hi")

say_hello()
say_hi()

# 3. Parameters vs Arguments

def say_hello_to_someone(name):
    print("Hello, " + name)

def multiply(number1, number2):
    print(number1 * number2)

multiply(4, 5)
say_hello_to_someone("Karla")

# 4. Print vs Return

def subtract(number1, number2):
    return number1 - number2

difference = subtract(10, 5)
print(difference)

print(subtract(20, 10))
