def main(actual_number, operator, number_to_process):
    try:
        calculator_use = get_user_promp('', 'Do you want to use the calculator? (yes, no): ')
        while calculator_use == 'yes':
            actual_number = 0
            print('Calculator: \n', actual_number)

            actual_number = int(get_user_promp('number', 'Insert the first number: '))
            print('Calculator: \n', actual_number)

            operator = get_user_promp('operator', 'Select the operator \n1: + \n2: - \n3: x \n4: / \n')
            print('Calculator: \n', actual_number)

            number_to_process = int(get_user_promp('number', 'Insert the second number: '))
            print('Calculator: \n', number_to_process)

            if operator == 1:
                print('Calculator: \n', add(actual_number, number_to_process))
            elif operator == 2:
                print('Calculator: \n', subtract(actual_number, number_to_process))
            elif operator == 3:
                print('Calculator: \n', multiply(actual_number, number_to_process))
            elif operator == 4:
                print('Calculator: \n', divide(actual_number, number_to_process))
            else:
                raise ValueError('Invalid Operator raised in main')
            calculator_use = get_user_promp('', 'Do you want to use the calculator again? (yes, no): ')
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

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    try:
        if number2 == 0:
            raise ZeroDivisionError('Error al dividir por cero raised in divide')
        return number1 / number2
    except ZeroDivisionError as ex:
        raise ex


if __name__ == '__main__':
    try:
        main(0,'+',0)
    except Exception as ex:
        print('error en Expetion general ',ex)