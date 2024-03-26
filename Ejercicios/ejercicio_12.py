class CuentaBancaria:
    def __init__(self, nombre_propietario, tipo_cuenta, saldo):
        self.__nombre_propietario = nombre_propietario
        self.__tipo_cuenta = tipo_cuenta
        self.__saldo = saldo

    def set_nombre_propietario(self, nombre_propietario):
        self.__nombre_propietario = nombre_propietario

    def get_nombre_propietario(self):
        return self.__nombre_propietario

    def set_tipo_cuenta(self, tipo_cuenta):
        self.__tipo_cuenta = tipo_cuenta

    def get_tipo_cuenta(self):
        return self.__tipo_cuenta

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("No hay suficientes fondos en la cuenta")

persona = CuentaBancaria(None, None, None)

persona.set_nombre_propietario('Abner')
persona.set_tipo_cuenta('Ahorro')
persona.set_saldo(4500)

nombre = persona.get_nombre_propietario()
tipo = persona.get_tipo_cuenta()
total = persona.get_saldo()

print(f'El nombre es: {nombre}')
print(f'El tipo de cuenta es: {tipo}')
print(f'El saldo de la cuenta es: {total}')

persona.depositar(500)
deposito = persona.get_saldo()
print(f'El saldo de la cuenta despues del deposito es: {deposito}')

persona.retirar(250)
retiro = persona.get_saldo()
print(f'El saldo de la cuenta despues del retiro es: {retiro}')