class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        cantidad = int(input('Ingresa la cantidad que deseas depositar: '))
        self.saldo += cantidad
        print(f'Se ha hecho un deposito de {cantidad} pesos')
    def retiro(self):
        cantidad = int(input('Ingresa la cantidad que deseas retirar: '))
        if cantidad > self.saldo:
            print('No tienes saldo suficiente para retirar esa cantidad.')
        else:
            self.saldo -= cantidad
            print(f'Se ha hecho un retiro de {cantidad} pesos')

    def informacion(self):
        print(f"""
        ---Informacion de la cuenta---
        Nombre del titular: {self.titular}
        Saldo disponible: {self.saldo} pesos
        """)

usuario = CuentaBancaria('Abner Arce', 100)

usuario.informacion()

usuario.depositar()

usuario.informacion()

usuario.retiro()

usuario.informacion()