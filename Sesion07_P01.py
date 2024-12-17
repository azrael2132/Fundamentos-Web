def registrar_gastos():
    gastos = []
    
    for dia in range(1, 8):
        gasto = float(input(f"Ingresa tu gasto del día {dia}: "))
        gastos.append(gasto)

    total = sum(gastos)
    print(f"El total de gastos de la semana es: ${total:.2f}")

registrar_gastos()
