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
