# Why do we need them? Demo

# Problems with this method:
#  1. It's hard to organize the data
#  2. It's hard to access the data

name = "Richard"
age = 36
has_pets = True

name_2 = "Lara"
age_2 = 26
has_pets_2 = False


# Create a dictionary

student = {
    "name": "Richard",
    "age": 36,
    "has_pets": True
}

print(student)

# Access a value in the dictionary
# print(student["name"])

# Add a key-value pair to the dictionary
student["country"] = "Germany"
print(student)

# Update a value in the dictionary
student["age"] = 37
print(student)

# Remove a key-value pair from the dictionary
del student["has_pets"]
print(student)

# Check if key exists
if "name" in student:
  print("Student has a name!")

# Iterate over the dictionary
for key, value in student.items():
    print(key, value)

