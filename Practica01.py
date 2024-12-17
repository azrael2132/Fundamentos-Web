
#numeros = list(range(1, 11))

numeros = [1,2,3,4,5,6,7,8,9,10]

print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

def filtrar_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return impares

impares = filtrar_impares(numeros)
print("Números impares:", impares)
