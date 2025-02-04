# Dadas las horas trabajadas de una persona y su tarifa por hora, calcular y mostrar su salario.

hour_fee =0
worked_hours=0
total_salary = 0

worked_hours = input('Ingrese las horas trabajadas:')
hour_fee = input('Ingrese su tarifa por hora:')

total_salary = int(worked_hours) * int(hour_fee)

print(f'Su salario es de {total_salary}')
