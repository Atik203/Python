class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def student_admission(self, student):
        classroom = student.classroom.name
        if classroom in self.classrooms:
            self.classrooms[classroom].add_student(student)
        else:
            print("Classroom not found")

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return "A+"
        elif marks >= 70:
            return "A"
        elif marks >= 60:
            return "A-"
        elif marks >= 50:
            return "B"
        elif marks >= 40:
            return "C"
        elif marks >= 33:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.50,
            "D": 1.00,
            "F": 0.00
        }
        return grade_map[grade]

    def __repr__(self) -> str:
        print('--------All Classrooms--------')
        for key, value in self.classrooms.items():
            print(key)

        print('--------Students--------\n')
        eight = self.classrooms['8th']
        print('------8th Classroom---------')
        for student in eight.students:
            print(student.name)

        print('------Subjects---------')
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        print('------Marks---------')
        for student in eight.students:
            print(student.name, student.marks, student.subject_grade)

        return ""


class Classroom:
    def __init__(self, name):
        self.name = name
        # composition
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students) + 1}'
        student.id = serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

    def __str__(self):
        return f'{self.name} has {len(self.students)} students'

    def get_top_students(self):
        pass


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
