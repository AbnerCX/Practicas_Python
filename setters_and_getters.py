class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

abner = Persona(None, 21)

nombre = input('Introduce tu nombre: ')

abner.setNombre(nombre)

nombre = abner.getNombre()

print(f'El nombre es: {nombre}')
