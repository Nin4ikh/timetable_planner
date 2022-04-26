
from src.subject import Subject

class Teacher:

    def __init__(self, teacher_id: int, name: str, subjects: list[Subject], extracourse: list = None):
        self.teacher_id = teacher_id
        self.name = name
        self.subjects = subjects
        self.extracourse = extracourse if extracourse is not None else []

