# simple_inheritance_3.py
# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
    
    def walk(self):
        print(f"{self.name} is speaks english")

# Child class - Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []
    
    def study(self):
        print(f"{self.name} is studying")
    
    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.name} got grade: {grade}")
    
    def introduce(self):
        super().introduce()
        print(f"I'm a student with ID: {self.student_id}")

# Child class - Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
    
    def introduce(self):
        super().introduce()
        print(f"I'm a {self.subject}  lecturer")

# Testing
print("\n" + "="*40)
print("SIMPLE INHERITANCE - PERSON")
print("="*40)

# Create student
student = Student("xyz", 24, "IS123")
print("\n--- Student ---")
student.introduce()
student.study()
student.add_grade(85)
student.walk()

# Create  lecturer
teacher = Teacher("Mr. shivakumar", 50, "CNS")
print("\n---  lecturer ---")
teacher.introduce()
teacher.teach()
teacher.walk()
