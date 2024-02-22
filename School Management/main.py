from School import School, Classroom, Subject
from Persons import Student, Teacher


def main():
    school = School("ABC School", "New York")

    eight = Classroom("8th")
    school.add_classroom(eight)
    nine = Classroom("9th")
    school.add_classroom(nine)
    ten = Classroom("10th")
    school.add_classroom(ten)

    abul = Student("Abul", eight)
    babul = Student("Babul", eight)

    school.student_admission(abul)
    school.student_admission(babul)

    teacher1 = Teacher("Mr. X")
    teacher2 = Teacher("Mr. Y")

    physics = Subject("Physics", teacher2)
    math = Subject("Math", teacher1)
    eight.add_subject(physics)
    eight.add_subject(math)

    eight.take_semester_final()
    print(school)


if __name__ == "__main__":
    main()
