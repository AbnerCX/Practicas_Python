from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def informacion_grado(self):
        print(f'''
        INFORMACION DEL ESTUDIANTE
        El grado del estudiante es: {self.grado} grado
        ''')
