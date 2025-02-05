from actions.StudentManager import StudentManager
from actions.GradeCalculator import GradeCalculator
from data.CsvHandler import CSVHandler

class Menu:
    def __init__(self):
        self.manager = StudentManager(['math', 'english', 'science'])
        self.calculator = GradeCalculator()
        self.csv_handler = CSVHandler()

    def display_menu(self):
        while True:
            try:
                option = int(input('''\n Please select an option:
                1. Add a student
                2. See all students information
                3. Top 3 highest grades
                4. The average grade of all students
                5. Export info to a CSV file
                6. Import info from a CSV file
                7. Exit
                \n'''))
                print(option.is_integer())
                if option == 1:
                    self.manager.add_student()
                elif option == 2:
                    self.manager.display_students()
                elif option == 3:
                    self.calculator.calculate_top_3(self.manager.get_students())
                elif option == 4:
                    avg = self.calculator.calculate_global_average(self.manager.get_students())
                    print(f"\n🎓 The global average grade is: {avg} 🎓\n")
                elif option == 5:
                    self.csv_handler.export_to_csv(self.manager.get_students())
                elif option == 6:
                    self.manager.students = self.csv_handler.import_from_csv()
                elif option == 7:
                    print("Exiting... 👋")
                    break
                else:
                    print("\n❌ Invalid option. Please select a valid option. ❌\n")
            except ValueError:
                print("\n❌ Invalid input. Please enter a number. ❌\n")
