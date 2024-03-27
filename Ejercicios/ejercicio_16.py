class Operaciones():
    def hacer_suma(self, numero_1, numero_2):
        operacion = numero_1 + numero_2
        return operacion

    def hacer_resta(self,numero_1, numero_2):
        operacion = numero_1 - numero_2
        return operacion

    def hacer_multiplicacion(self, numero_1, numero_2):
        operacion = numero_1 * numero_2
        return operacion

    def hacer_divicion(self, numero_1, numero_2):
        if numero_2 != 0:
            operacion = numero_1 / numero_2
            return operacion
        else:
            print('No se puede dividir entre cero.')
            return None

def calculadora():

    calculo = Operaciones()

    while True:

        print('1- Suma')
        print('2- Resta')
        print('3- Multiplicacion')
        print('4- Division')
        print('5- Salir')

        try:
            opcion = int(input('Introduce la operacion que deseas realizar: '))

            if opcion == 1:
                print('----Has seleccionado Suma-----')
                numero_1 = int(input('Introduce el primer numero: '))
                numero_2 = int(input('Introduce el segundo numero: '))
                resultado = calculo.hacer_suma(numero_1, numero_2)
                print(f'El resultado de la operacion es: {resultado}')
            elif opcion == 2:
                print('----Has seleccionado Resta-----')
                numero_1 = int(input('Introduce el primer numero: '))
                numero_2 = int(input('Introduce el segundo numero: '))
                resultado = calculo.hacer_resta(numero_1, numero_2)
                print(f'El resultado de la operacion es: {resultado}')
            elif opcion == 3:
                print('----Has seleccionado Multiplicacion----')
                numero_1 = int(input('Introduce el primer numero: '))
                numero_2 = int(input('Introduce el segundo numero: '))
                resultado = calculo.hacer_multiplicacion(numero_1, numero_2)
                print(f'El resultado de la operacion es: {resultado}')
            elif opcion == 4:
                print('----Has seleccionado Division----')
                numero_1 = float(input('Introduce el primer numero: '))
                numero_2 = float(input('Introduce el segundo numero: '))
                resultado = calculo.hacer_divicion(numero_1, numero_2)
                if resultado is None:
                    continue
                else:
                    print(f'El resultado de la operacion es: {resultado}')
            elif opcion == 5:
                return False

        except ValueError:
            print('Introduce un numero valido.')

calculadora()