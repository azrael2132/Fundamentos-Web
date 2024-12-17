def contar_palabras():
    frase = input("Ingresa una frase: ")
    palabras = frase.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    palabra_mas_repetida = max(frecuencia, key=frecuencia.get)
    conteo_total = len(palabras)

    print("Total de palabras:", conteo_total)
    print("La palabra que más se repite es:", palabra_mas_repetida)

contar_palabras()
