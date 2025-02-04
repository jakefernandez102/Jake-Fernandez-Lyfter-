from actions.student import add_student, get_students_info, set_students
from actions.calculations import calculate_top_3_average_grades, calculate_global_average_students_grades
from data.export_to_csv import export_student_list_to_csv
from data.import_from_csv import import_from_csv

def trigger_action(user_option):
    if user_option == 1:
        print("\n📝 Adding a student...\n")
        add_student()
    if user_option == 2:
        print("\n Printing students info...\n")
        print(get_students_info())
    if user_option == 3:
        print("\nPrinting top 3 grades...\n")
        students = get_students_info()
        calculate_top_3_average_grades(students)
    if user_option == 4:
        print("\nAverage of all students grades...\n")
        students = get_students_info()
        average = calculate_global_average_students_grades(students)
        print(f"\n🎓 The average of all students grades is: {average} 🎓\n")
    if user_option == 5:
        print("\nExporting to csv...\n")
        students = get_students_info()
        export_student_list_to_csv(students)
    if user_option == 6:
        print("\nImporting from csv...\n")
        students = import_from_csv()
        set_students(students)
