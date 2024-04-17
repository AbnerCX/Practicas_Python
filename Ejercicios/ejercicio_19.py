
class Estudiante:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def agregar_calificaciones(self):
        lista = []
        resultado = 0

        total = int(input('Introduce cuantas calificaciones deseas agregar: '))

        for i in range(total):
            calificacion = int(input(f'Agrega la calificación número {i + 1}: '))
            lista.append(calificacion)
        for x in lista:
            resultado += x

        promedio = resultado / len(lista)
        print(f'El promedio de tu calificaion es: {promedio:.2f}')
        return promedio

    def mostrar_informacion(self, promedio):
        print(f'''
        Nombre: {self._nombre}
        Edad: {self._edad}
        Promedio: {promedio:.2f}
            ''')

estudiante_1 = Estudiante('Abner', 21)
total = estudiante_1.agregar_calificaciones()
estudiante_1.mostrar_informacion(total)