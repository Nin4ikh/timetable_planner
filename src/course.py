
from src.schoolclass import Schoolclass
from src.teacher import Teacher
from src.subject import Subject


class Course:
    """
    A course is a unit of a timetable. It must be held by a teacher with the
    needed capability
    """
    def __init__(self, course_id: int, name: str, teacher: Teacher, capability: Subject, schoolclass: Schoolclass):
        self.course_id = course_id  # new continueing ID
        self.name = name
        self.teacher = teacher
        self.capability = capability
        self.schoolclass = schoolclass
