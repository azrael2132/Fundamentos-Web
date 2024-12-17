def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros_primos = []
contador = 0

for num in range(1, 100):
    if es_primo(num):
        numeros_primos.append(num)
        contador += 1

print("Los números primos:", numeros_primos)
print("El total de números primos:", contador)