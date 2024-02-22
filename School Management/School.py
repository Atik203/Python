class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}


    def add_teacher(self,subject, teacher):
        self.teachers[subject] = teacher

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def student_admission(self, student, classroom_room):
        if classroom_room in self.classrooms:
            self.classrooms[classroom_room].add_student(student)
        else:
            print("Classroom not found")


class Classroom:
    def __init__(self, name):
        self.name = name
        # composition
        self.students = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)

    def __str__(self):
        return f'{self.name} has {len(self.students)} students'

    def get_top_students(self):
        pass
