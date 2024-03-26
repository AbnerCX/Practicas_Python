class Estudiante:

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')

nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')
grado = input('Introduce tu grado: ')

estudiante = Estudiante(nombre, edad, grado)

print(f'El nombre del estudiante es: {estudiante.nombre}')
print(f'La edad del estudiante es: {estudiante.edad}')
print(f'El grado del estudiante es: {estudiante.grado}')

estudiante.estudiar()