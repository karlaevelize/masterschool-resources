# 1. Write a function that prints out "Hello, World!" 10 times.

def print_hello():
    print("Hello, World!" * 10)

print_hello()

# 2. Modify the function so that it takes an argument n and prints out "Hello, World!" n times.

def print_hello_n_times(n):
    print("Hello, World!" * n)

print_hello_n_times(2)

# 3. Write a function called `sum` that takes two arguments and returns their sum.

def sum(number1, number2):
    return number1 + number2

# 4. Write a function called `square` that takes one argument and returns its square.

def square(number):
    return number * number

# 5. Write a function called `larger` that takes two arguments and returns the larger one.

def larger(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

# 6. Write a function called `calculate_circle_area` that takes one argument (the radius of a circle) and returns the area of the circle.

def calculate_circle_area(r):
    PI = 3.14
    area = 3.14 * (r * r)
    return area

# 7. Write a function called `average` that takes two numbers as arguments and returns the average of those numbers.

def average(number1, number2):
    return (number1 + number2) / 2

# 8. Write a function called `greet` that takes a name as an argument and returns a greeting message.

def greet(name):
    return "Hello, " + name

# 9. Write a function called `is_even` that takes a number as an argument and returns `The number is even` if the number is even and `The number is odd` if the number is odd.

def is_even(number):
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"


# 10. Write a function called `apply_discount` that takes the price of a product and a discount percentage and returns the final price of the product after the discount.