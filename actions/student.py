students = []
topics = ['math', 'english', 'science']

def set_students(students_list):
    global students 
    students = students_list

def add_student():
    wants_to_add = input("Do you want to add a student? (y/n): ")

    if( wants_to_add.lower() != 'y' and wants_to_add.lower() != 'n'):
        print("Please enter a valid option")
        return add_student()
    elif wants_to_add.lower() == 'n':
        print("No students added")
        return

    while wants_to_add.lower() == 'y':
        student = request_student_info()
        students.append(student)
        wants_to_add = input("Do you want to add another student? (y/n): ")
    print("Students added successfully! ✅")
    print(students)


def request_student_info():
    student = {}
    student['name'] = input("Enter the student's name: ")
    student['group'] = input("Enter the student's group: ")
    student['grades']= request_grades()
    print(student)
    return student

def request_grades():
    student_grades = []
    topic_grade = {}
    try:
        for topic in topics:
            grade = is_valid_grade(input(f"Enter the student's grade in {topic}: "))
            topic_grade[topic] = grade
        student_grades.append(topic_grade)
        return student_grades
    except ValueError as ex:
        raise ex

def is_valid_grade(grade):
    if not grade.isdigit():
        raise ValueError("Please enter a valid grade it must be number.")
    grade = int(grade)
    if grade < 0 or grade > 100:
        raise ValueError("Please enter a valid grade between 0 and 100.")
    return grade

def get_students_info():
    if not students:
        print("\n∅ No students to display.\n")
        return
    return students
