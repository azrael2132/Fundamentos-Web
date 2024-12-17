def calcular_promedio():
    # Solicitar las calificaciones
    calificacion1 = float(input("Ingresa la primera calificación: "))
    calificacion2 = float(input("Ingresa la segunda calificación: "))
    calificacion3 = float(input("Ingresa la tercera calificación: "))

    promedio = (calificacion1 + calificacion2 + calificacion3) / 3

    if promedio >= 20:
        resultado = "Aprobado"
    else:
        resultado = "Reprobado"

    print(f"Promedio: {promedio:.2f} - Resultado: {resultado}")

calcular_promedio()
