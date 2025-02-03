# Dado el nombre y apellido de un empleado, y el dominio .com de una empresa, genere su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.

first_name = input('Ingrese su primer nombre:')
surname = input('Ingrese su apellido:')
company_domain = input('Ingrese el dominio de su empresa:')

email_address = f'{first_name}.{surname}@{company_domain}.com'

print(f'Your company email is: {email_address}')