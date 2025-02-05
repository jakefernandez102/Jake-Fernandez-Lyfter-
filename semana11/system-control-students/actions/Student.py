class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, Group: {self.group}, Grades: {self.grades}"
