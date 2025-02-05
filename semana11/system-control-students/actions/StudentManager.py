from actions.Student import Student

class StudentManager:
    def __init__(self,topics):
        self.students = []
        self.topics = topics

    def add_student(self):
        name = input("Enter student's name: ")
        group = input("Enter student's group: ")
        grades = self.request_grades()
        student = Student(name, group, grades)
        self.students.append(student)
        print(f"\n✅ {name} has been added successfully!\n")

    def request_grades(self):
        grades = {}
        for topic in self.topics:
            while True:
                try:
                    grade = int(input(f"Enter {topic} grade: "))
                    if 0 <= grade <= 100:
                        grades[topic] = grade
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric grade.")
        return grades

    def display_students(self):
        if not self.students:
            print("\n∅ No students available.\n")
        else:
            for student in self.students:
                print(student)

    def get_students(self):
        return self.students
