from actions.trigger_action import trigger_action

def menu():
    while True:
        try:
            user_option = int(input(' Please select an option: \n 1. Add a student \n 2. See all students information \n 3. Top 3 higher grades.  \n 4. The average of the grade point average of all students. \n 5. Export info to a csv file. \n 6. Import info from a csv file. \n\n'))

            if 1 <= user_option <= 6:
                trigger_action(user_option)
            else:
                print("\n❌Invalid option, Please select a valid option❌\n")
        except ValueError as ex:
            raise ex
