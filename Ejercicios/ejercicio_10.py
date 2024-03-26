class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def informacion(self):
        print(f'''
        INFORMACION DEL ESTUDIANTE
        Nombre: {self.nombre}
        Edad: {self.edad}
        ''')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def informacion_grado(self):
        print(f'''
        INFORMACION DEL ESTUDIANTE
        El grado del estudiante es: {self.grado} grado
        ''')

estudiante_1 = Estudiante('Abner', 20, 3)

estudiante_1.informacion()
estudiante_1.informacion_grado()
