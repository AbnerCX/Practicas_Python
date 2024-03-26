class CuentaBancaria:
    def __init__(self, nombre, edad, saldo_inicial=0):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def consultar_saldo(self):
        return self.saldo
