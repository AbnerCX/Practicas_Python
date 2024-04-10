class Animal:
    def __init__(self, nombre, edad, especie):
        self._nombre = nombre
        self._edad = edad
        self._especie = especie

    def mostrar_informacion(self):
        print(f'''
        Especie: {self._especie}
        Nombre: {self._nombre}
        Edad: {self._edad}
        ''')

class Perro(Animal):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre,edad,especie)
        self._raza = raza

    def ladrar(self):
        print(f'El perro {self._nombre} esta ladrando')

    def mostrar_informacion(self):
        print(f'''
        Especie: {self._especie}
        Nombre: {self._nombre}
        Edad: {self._edad}
        Raza: {self._raza}
        ''')

class Gato(Animal):
    def __init__(self, nombre, edad, especie, raza, color):
        super().__init__(nombre,edad,especie)
        self._raza = raza
        self._color = color

    def maullar(self):
        print(f'El gato {self._nombre} esta maullando')

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, raza):
        self._raza = raza

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def mostrar_informacion(self):
        print(f'''
        Especie: {self._especie}
        Nombre: {self._nombre}
        Edad: {self._edad}
        Raza: {self._raza}
        Color: {self._color}
        ''')


animal1 = Animal('Abner', 21, 'Humano')
animal1.mostrar_informacion()

animal2 = Perro('Abisai', 22, 'Canino', 'Pug')
animal2.mostrar_informacion()

animal3 = Gato('Kiry', 10, 'Felino', 'Siames', 'Blanco')
animal3.mostrar_informacion()


print(animal3.color)
animal3.color = 'Amarillo'
print(animal3.color)