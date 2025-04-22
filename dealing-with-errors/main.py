# Exercise 1: 📊 Calculate average

num1 = 10
num2 = 20
num3 = 30

total = num1 + num2 + num3
average = total / 3

print(f"The total is {total} and the average is {average}.")

# Exercise 2: 🔲 Area and Perimeter

length = 5.5
width = 3

area = length * width
perimeter = 2 * (length + width)

print(f"The area is {area} and the perimeter is {perimeter}.")

# Exercise 3: 5️⃣ Multiply

def multiply(num1, num2):
    product = num1 * num2
    return f"The result of multiplying {num1} and {num2} is {product}."

print(multiply(5, 10))

# Exercise 4: 📖 Reading Time

def reading_time_calculator(number_of_pages):
    time_per_page_in_seconds = 20
    total_time_in_seconds = number_of_pages * time_per_page_in_seconds
    hours = total_time_in_seconds // 3600
    minutes = (total_time_in_seconds % 3600) // 60
    seconds = total_time_in_seconds % 60

    return f"The book has {number_of_pages} pages. Total reading time: {hours} hours, {minutes} minutes, and {seconds} seconds."

print(reading_time_calculator(50))