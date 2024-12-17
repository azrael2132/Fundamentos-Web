# Inicializa una lista vacía
numeros = []

# Pide al usuario que ingrese números
while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)  # Convierte la entrada a un número
        numeros.append(numero)    # Agrega el número a la lista
    except ValueError:
        print("Por favor, ingresa un número válido.")
   
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

contador_par = sum(1 for x in numeros if x % 2 == 0)  # Contador de números pares
contador_impar = sum(1 for x in numeros if x % 2 != 0)  # Contador de números impares

print("Los numeros pares son: ", pares)
print("Los numeros impares son: ", impares)
print("Numeros Impares son: ", contador_impar)
print("Numeros Impares son: ", contador_par)