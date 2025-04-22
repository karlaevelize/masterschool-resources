# Exercise 3
student_grades = {
    "emma_schneider": [88, 92, 79],
    "jonas_muller": [76, 81, 85],
    "ben_fischer": [90, 87, 93],
    "felix_wagner": [72, 75, 70],
    "lena_hoffmann": [95, 89, 91]
}

# Calculate and print the best grade for each student. The best grade is the highest grade in the list for that student.
best_grades = dict()

for key, value in student_grades.items():
    best_grades[key] = max(value)

print(best_grades)


# Calculate and print the average grade for each student across all subjects, rounded down to the nearest whole number, e.g, 86.7 → 86 (hint: use builtin list operations)


# Create a function find_top_student(student_grades) that: Accepts the dictionary student_grades. Returns the name of the student with the highest average grade.


