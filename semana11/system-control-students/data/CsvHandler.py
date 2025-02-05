import csv
from actions.Student import Student

class CSVHandler:
    @staticmethod
    def export_to_csv(students, filename="students_info.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Group", "Math", "English", "Science"])
            for student in students:
                writer.writerow([student.name, student.group, *student.grades.values()]) #unpack the greades values to store it as individual columns 
        print("\n📂 Students data exported successfully!\n")

    @staticmethod
    def import_from_csv(filename="students_info.csv"):
        students = []
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grades = CSVHandler.convert_grades(row)
                    students.append(Student(row["Name"], row["Group"], grades))
            print("\n📥 Students data imported successfully!\n")
        except FileNotFoundError:
            print("\n❌ CSV file not found.\n")
        return students

    @staticmethod
    def convert_grades(row):
        grades = {}
        for key, value in row.items():
            if key not in ["Name", "Group"]:
                grades[key] = int(value)
        return grades
