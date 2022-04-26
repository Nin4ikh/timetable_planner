
from src.schoolclass import Schoolclass
from src.teacher import Teacher
from src.student import Student
from src.subject import Subject

# TODO: create all pupils, teachers, classes and courses by reading from a database

if __name__ == '__main__':
    # create classes
    class_1a = Schoolclass(1, "a")
    class_1b = Schoolclass(1, "b")

    # create pupils and put them in classes
    maximilian = Student(1, "Max", 1, "a")
    maria = Student(2, "Maria", 1, "a")
    maria2 = Student(3, "Maria", 1, "b")
    peter = Student(4, "Peter", 1, "b")

    ###

    # create capabilities
    maths1 = Subject(1, "Maths", grades=[1, 2])
    english1 = Subject(2, "English", grades=[1, 2])
    spanish1 = Subject(3, "Spanish", grades=[1, 2])

    # create teachers
    mr_thompson = Teacher(1, "Mr Thompson", subjects=[maths1, english1])
    mrs_thompson = Teacher(2, "Mrs Thompson", subjects=[maths1, spanish1])

    ###

    # create courses

    # create timetable
