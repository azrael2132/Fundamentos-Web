import csv


archivo_csv = 'empleados.csv'
contenido = """nombre,edad,salario,departamento
Ana,34,3000,IT
Luis,28,2500,Marketing
Carla,45,4000,Finanzas
Jorge,38,3200,IT
Elena,30,2700,Marketing
"""


with open(archivo_csv, 'w', newline='') as archivo:
    archivo.write(contenido)


def leer_empleados(archivo):
    empleados = []
    with open(archivo, mode='r', newline='') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            empleados.append(fila)
    return empleados

def empleados_por_departamento(empleados, departamento):
    return [empleado['nombre'] for empleado in empleados if empleado['departamento'] == departamento]

def salario_promedio(empleados, departamento):
    salarios = [int(empleado['salario']) for empleado in empleados if empleado['departamento'] == departamento]
    return sum(salarios) / len(salarios) if salarios else 0

empleados = leer_empleados(archivo_csv)

empleados_it = empleados_por_departamento(empleados, 'IT')
salario_promedio_it = salario_promedio(empleados, 'IT')

empleados_marketing = empleados_por_departamento(empleados, 'Marketing')
salario_promedio_marketing = salario_promedio(empleados, 'Marketing')


print("Empleados en el departamento de IT:", empleados_it)
print("Salario promedio en IT:", salario_promedio_it)
print("Empleados en el departamento de Marketing:", empleados_marketing)
print("Salario promedio en Marketing:", salario_promedio_marketing)
