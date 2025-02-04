from actions.student import topics

def calculate_top_3_average_grades(students ):
    if not students:
        return 0
    top_3_grades = {}
    students_average = {}
    average = 0
    for index,student in enumerate(students):
        print(f"\nStudent {index + 1}: {student['name']}")
        average = 0
        for topic in topics:
            average += student['grades'][0][topic]
            print(average)
        average = average / len(topics)
        students_average[student['name']] = round(average,1)
        print(average)
        print(students_average)

    top_3_grades = assign_top_3_grades(students_average)

    print(f"\nThe top 3 grades are: {top_3_grades}\n")

def assign_top_3_grades(students_average):
    medals = ['🥇', '🥈', '🥉']
    top_3_grades = {}
    sorted_students = sorted(students_average.items(), key=lambda x: x[1], reverse=True)

    for idx, (name, grade) in enumerate(sorted_students[:3]):
        if idx < 3:
            top_3_grades[medals[idx]] = {name: grade}

    return top_3_grades


def calculate_global_average_students_grades(students):
    if not students:
        return 0
    average = 0
    for student in students:
        for topic in topics:
            average += student['grades'][0][topic]
    average = average / (len(students) * len(topics))
    return round(average, 1)