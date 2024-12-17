
lista_de_sublistas = [
    [1, "manzana", 3],
    ["naranja", 4, "manzana"],
    [5, 6, 7, 6],
    ["platano", 9, 1, 5]
]

def elementos_unicos(lista_de_sublistas):
    frecuencia = {}
    
    for sublista in lista_de_sublistas:
        for elemento in sublista:
            if elemento in frecuencia:
                frecuencia[elemento] += 1
            else:
                frecuencia[elemento] = 1
                
    unicos = [elemento for elemento, cuenta in frecuencia.items() if cuenta == 1]
    return unicos

elementos_unicos_lista = elementos_unicos(lista_de_sublistas)
print("Elementos únicos:", elementos_unicos_lista)
   