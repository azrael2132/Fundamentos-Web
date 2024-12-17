import csv

data = [
    ["Nombre", "Edad", "Grado"],
    ["Juan", 15, 10],
    ["María", 14, 9],
    ["Pedro", 16, 11],
    ["Luisa", 15, 10]
]

with open('estudiantes.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

estudiantes = []
with open('estudiantes.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        estudiantes.append(row)

print("Estudiantes mayores de 15 años:")
for estudiante in estudiantes:
    if int(estudiante['Edad']) > 15:
        print(estudiante['Nombre'])
