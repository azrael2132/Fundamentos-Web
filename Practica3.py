suma = 0

# Sumar números
while True:
    numero = input("Ingresa un número para sumar (o escribe 'salir' para terminar): ")
    
    if numero.lower() == 'salir':
        break  # Salir del bucle si el usuario escribe 'salir'
    
    try:
        suma += float(numero)  # Convertir a número y agregar a la suma
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Solicitar un número para multiplicar
multiplicador = input("Ingresa un número para multiplicar la suma total: ")
try:
    resultado = suma * float(multiplicador)
    print(f"La suma total es: {suma}")
    print(f"El resultado de la suma multiplicada por {multiplicador} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido para multiplicar.")
    