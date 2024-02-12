class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"

class School:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class College:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"

class Student(School, College):
    def __init__(self, name, age, grade, course):
        School.__init__(self, name, age, grade)
        College.__init__(self, name, age, course)

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Course: {self.course}"

student = Student('Rahul', 20, 12, 'B.Tech')
print(student)
