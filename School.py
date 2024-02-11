class Student:
    def __init__(self, name, id, current_class):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self):
        return f"Student: ({self.name},{self.id},{self.current_class})"

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.id = id
        self.subject = subject

    def __repr__(self):
        return f"Teacher: ({self.name},{self.subject})"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        self.teachers.append(Teacher(name, subject, id))

    def enroll(self, name, fee):
        if fee < 6500:
            return "Fee is less than 6500"
        else:
            id = len(self.students) + 1001
            self.students.append(Student(name, id, 12))
            return f"Enrolled Successfully and Extra money {fee - 6500} is returned"

    def __repr__(self):
        result = f"Welcome To: {self.name}\n"
        result += "***************Teachers***************\n"
        for teacher in self.teachers:
            result += str(teacher) + "\n"
        result += "***************Students***************\n"
        for student in self.students:
            result += str(student) + "\n"
        return result


atik = School("Atik School")
atik.add_teacher("John", "Maths")
atik.add_teacher("Doe", "Physics")
atik.enroll("Atik", 9000)
atik.enroll("Alex", 6000)
print(atik)
