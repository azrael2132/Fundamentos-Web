class CuentaBancaria:
    def __init__(self, nombre, apellido, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.profesion = profesion
        self.saldo_soles = 0.0
        self.saldo_dolares = 0.0

    def depositar(self, cantidad, divisa):
        if divisa.lower() == "soles":
            if cantidad > 0:
                self.saldo_soles += cantidad
                print(f"Se han depositado S/{cantidad:.2f}. Nuevo saldo en soles: S/{self.saldo_soles:.2f}")
            else:
                print("La cantidad a depositar debe ser positiva.")
        elif divisa.lower() == "dolares":
            if cantidad > 0:
                self.saldo_dolares += cantidad
                print(f"Se han depositado ${cantidad:.2f}. Nuevo saldo en dólares: ${self.saldo_dolares:.2f}")
            else:
                print("La cantidad a depositar debe ser positiva.")
        else:
            print("Divisa no válida. Use 'soles' o 'dolares'.")

    def retirar(self, cantidad, divisa):
        if divisa.lower() == "soles":
            if cantidad > 0 and cantidad <= self.saldo_soles:
                self.saldo_soles -= cantidad
                print(f"Se han retirado S/{cantidad:.2f}. Nuevo saldo en soles: S/{self.saldo_soles:.2f}")
            elif cantidad > self.saldo_soles:
                print("Fondos insuficientes en soles.")
            else:
                print("La cantidad a retirar debe ser positiva.")
        elif divisa.lower() == "dolares":
            if cantidad > 0 and cantidad <= self.saldo_dolares:
                self.saldo_dolares -= cantidad
                print(f"Se han retirado ${cantidad:.2f}. Nuevo saldo en dólares: ${self.saldo_dolares:.2f}")
            elif cantidad > self.saldo_dolares:
                print("Fondos insuficientes en dólares.")
            else:
                print("La cantidad a retirar debe ser positiva.")
        else:
            print("Divisa no válida. Use 'soles' o 'dolares'.")

    def consultar_saldo(self):
        print(f"Saldo actual en soles: S/{self.saldo_soles:.2f}")
        print(f"Saldo actual en dólares: ${self.saldo_dolares:.2f}")

    def cambiar_divisa(self, cantidad, de_divisa, a_divisa, tasa_cambio):
        if de_divisa.lower() == "soles" and cantidad > 0:
            if cantidad <= self.saldo_soles:
                cantidad_dolares = cantidad / tasa_cambio
                self.saldo_soles -= cantidad
                self.saldo_dolares += cantidad_dolares
                print(f"Se han cambiado S/{cantidad:.2f} a ${cantidad_dolares:.2f} usando una tasa de cambio de {tasa_cambio:.2f}.")
            else:
                print("Fondos insuficientes en soles.")
        elif de_divisa.lower() == "dolares" and cantidad > 0:
            if cantidad <= self.saldo_dolares:
                cantidad_soles = cantidad * tasa_cambio
                self.saldo_dolares -= cantidad
                self.saldo_soles += cantidad_soles
                print(f"Se han cambiado ${cantidad:.2f} a S/{cantidad_soles:.2f} usando una tasa de cambio de {tasa_cambio:.2f}.")
            else:
                print("Fondos insuficientes en dólares.")
        else:
            print("La cantidad a cambiar debe ser positiva y la divisa debe ser 'soles' o 'dolares'.")

    def imprimir_voucher(self):
        print("\n--- Voucher ---")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Profesión: {self.profesion}")
        print(f"Saldo en soles: S/{self.saldo_soles:.2f}")
        print(f"Saldo en dólares: ${self.saldo_dolares:.2f}")
        print("----------------")
   
cuenta = CuentaBancaria("Sebastian", "Torres", "Ingeniero")
cuenta.depositar(10000, "soles")
cuenta.depositar(300, "dolares")
cuenta.retirar(200, "soles")
cuenta.consultar_saldo()
cuenta.cambiar_divisa(5000, "soles", "dolares", 3.5) 
cuenta.cambiar_divisa(100, "dolares", "soles", 3.5) 
cuenta.imprimir_voucher()
