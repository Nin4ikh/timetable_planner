
from src.schoolclass import Schoolclass


class Student:

    def __init__(self, student_id: int, name: str, grade: int, class_name: str, extracourse: list = None):
        self.student_id = student_id  # new continueing ID
        self.name = name
        self.grade = grade
        self.class_name = class_name
        self.extracourse = extracourse if extracourse is not None else []
