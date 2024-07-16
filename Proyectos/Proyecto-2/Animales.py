from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, nombre = None, edad= None, raza=None):
        self._nombre = nombre
        self._edad = edad
        self._raza = raza

    @abstractmethod
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def __init__(self, nombre=None, edad=None, raza=None):
        super().__init__(nombre,edad,raza)
    
    def agregar_datos(self):
        nombre = input("Introduce el Nombre: ")
        nombre = nombre.title()
        nombre = self._nombre

        edad = int(input("Introduce la edad: "))
        edad = self._edad

        raza = input("Introduce la raza: ")
        raza = raza.title()
        raza = self._raza

    def mostrar_informacion(self):
        print(f"""
        Nombre: {self._nombres} 
        Edad: {self._edad}
        Raza: {self._raza}
        """)

    def hacer_sonido(self):
        return "Guau!!"



class Gato(Animal):
    def __init__(self, nombre=None, edad=None, raza=None):
        super().__init__(nombre, edad, raza)

    def agregar_datos(self):
        nombre = input("Introduce el Nombre: ")
        nombre = nombre.title()
        nombre = self._nombre

        edad = int(input("Introduce la edad: "))
        edad = self._edad

        raza = input("Introduce la raza: ")
        raza = raza.title()
        raza = self._raza

    def mostrar_informacion(self):
        print(f"""
        Nombre: {self._nombres} 
        Edad: {self._edad}
        Raza: {self._raza}
        """)

    def hacer_sonido(self):
        return "Meow!!"
    
