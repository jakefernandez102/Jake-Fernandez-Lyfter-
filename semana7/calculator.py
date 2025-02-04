def main(actual_number, operator):
    try:
        calculator_use = get_user_promp('', 'Do you want to use the calculator? (y/n): ')
        current_number = 0
        while calculator_use == 'y':
            print('Calculator: \n', current_number)
            operator = get_user_promp('operator', 'Select the operator \n1: + \n2: - \n3: x \n4: / \n0: C \n')

            if operator == 0:
                current_number = 0
                continue

            number_to_process = get_user_promp('number', 'Enter the number to calculate: ')

            if operator == 1:
                current_number = add(current_number, number_to_process)
                print('Calculator: \n', current_number)
            elif operator == 2:
                current_number = subtract(current_number, number_to_process)
                print('Calculator: \n', current_number)
            elif operator == 3:
                current_number = multiply(current_number, number_to_process)
                print('Calculator: \n', current_number)
            elif operator == 4:
                current_number = divide(current_number, number_to_process)
                print('Calculator: \n', current_number)
            else:
                raise ValueError('Invalid Operator raised in main')
            calculator_use = get_user_promp('', 'Do you want to use the calculator again? (y/n): ')
    except ValueError as ex:
        raise ex

def get_user_promp(prompt_type, query):
    try:
        if prompt_type == 'number':
            return float(input(query))
        elif prompt_type == 'operator':
            return int(input(query))
        else:
            return input(query)
    except ValueError:
        raise ValueError('Invalid number value raised in get user prompt')

def add(current_number, number_to_process):
    return current_number + number_to_process

def subtract(current_number, number_to_process):
    return current_number - number_to_process

def multiply(current_number, number_to_process):
    return current_number * number_to_process

def divide(current_number, number_to_process):
    try:
        if number_to_process == 0:
            raise ZeroDivisionError('Error al dividir por cero raised in divide')
        return current_number / number_to_process
    except ZeroDivisionError as ex:
        raise ex


if __name__ == '__main__':
    try:
        main(0,'+')
    except Exception as ex:
        print('error en Expetion general ',ex)