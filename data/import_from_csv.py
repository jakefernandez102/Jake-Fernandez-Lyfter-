import csv
import json

def import_from_csv():
    students = []
    try:
        with open('students_info.csv', 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row)
                row["grades"] = json.loads(row["grades"])
                students.append(row)
        print("\nStudents info imported from csv successfully! ✅\n")
        return students

    except FileNotFoundError:
        print("\n🚨 No students to import 🚨\n")
