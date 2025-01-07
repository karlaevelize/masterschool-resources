# Learning about OOP in Python
# 1. Create a class called "Student": name, age, grade

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_student(self):
        return self.name, self.age, self.grade
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade
        

# Create an instance of a class
student1 = Student("Ana", 25, 75)
student2 = Student("Benjamin", 25, 20)

# I want to see the student object
print(student1.get_grade())
student1.set_grade(5)
print(student1.get_grade())