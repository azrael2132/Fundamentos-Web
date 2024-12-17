def verificar_edad():

    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    if edad >= 18:
        estado = "mayor de edad"
    else:
        estado = "menor de edad"

    print(f"{nombre}, eres {estado}.")
    
verificar_edad()
