import csv
import json

def export_student_list_to_csv(students):
    if not students:
        print("\n🚨 No students to export 🚨\n")
        return

    with open('students_info.csv', 'w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ["name", "group", "grades"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            writer.writerow({
                "name": student['name'],
                "group": student['group'],
                "grades": json.dumps(student['grades'])
            })
    print("\nStudents info exported to csv successfully! ✅\n")
