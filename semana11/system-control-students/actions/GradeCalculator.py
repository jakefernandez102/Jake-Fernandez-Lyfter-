class GradeCalculator:
    @staticmethod
    def calculate_top_3(students):
        if not students:
            print("No students available.")
            return

        sorted_students = sorted(students, key=lambda s: s.get_average(), reverse=True)
        medals = ['🥇', '🥈', '🥉']

        print("\n🏆 Top 3 Students:")
        for i, student in enumerate(sorted_students[:3]):
            print(f"{medals[i]} {student.name} - Average: {student.get_average():.2f}")

    @staticmethod
    def calculate_global_average(students):
        if not students:
            print("No students available.")
            return 0
        total_grades = sum(student.get_average() for student in students)
        return round(total_grades / len(students), 2)
