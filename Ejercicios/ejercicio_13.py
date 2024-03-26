class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def informacion(self):
        print('Informacion de la Persona')
        print(f'Nombre: {self._nombre}')
        print(f'Edad: {self._edad}')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

class PersonaEmail(Persona):
    def __init__(self, nombre, edad, email):
        super().__init__(nombre,edad)
        self._email = email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def informacion(self):
        print('Informacion de la Persona')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Email: {self.email}')

class Coche:
    def __init__(self, nombre, modelo, marca):
        self.nombre = nombre
        self.modelo = modelo
        self.marca = marca

    def informacion_coche(self):
        print('Informacion del coche')
        print(f'nombre: {self.nombre}')
        print(f'marca: {self.marca}')
        print(f'modelo: {self.modelo}')

persona1 = Persona('Abner', 21)
print(persona1.nombre)

persona2 = PersonaEmail('Abisai', 21, 'abner@gmail.com')
print(persona2.email)

coche1 = Coche('Perre', 'March', 'Nissan')
print(coche1.marca)