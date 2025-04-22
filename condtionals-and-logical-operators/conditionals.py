# 1. We have situation: the customer can only enter if they are 18 or older.

customer_age = 18

if customer_age >= 18:
    print("Welcome")
else:
    print("You are too young! :)")

# 2. I need to let my users know if they are a child, adult or elderly person.

user_age = 64

if user_age >= 65:
    print("Elderly")
elif user_age >= 18:
    print("Adult")
elif user_age >= 13:
    print("Teenager")
else:
    print("Child")

# 3. I want to have a barbecue: temperature must be above 25 and it must be weekend.

temperature_in_celsius = 27
is_weekend = True

if temperature_in_celsius > 25 and is_weekend:
    print("Let's have a BBQ!")
else:
    print("Not today :(")

# 4. I should take a coat if it's cold or if it's raining.

is_raining = True

if temperature_in_celsius < 15 or is_raining:
    print("Don't forget your coat!")
else:
    print("You don't need a coat today :)")

# Check if empty

# 1. Check the length of the string
# 2. Check if the string is == ""
