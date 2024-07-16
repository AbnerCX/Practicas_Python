from abc import ABC, abstractmethod

#PLANTILLA
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en: {self.actividad}')

abner = Estudiante("Abner", 22, "Hombre", "Programacion")
pedrito = Trabajador("Pedrito", 21, "Hombre", "Programacion")

abner.presentarse()
abner.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()


