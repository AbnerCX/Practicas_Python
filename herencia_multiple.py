class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('Hola estoy hablando un poco')

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def trabajar(self):
        print('Hola estoy trabajando')

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola mi nombre es: {self.nombre}, {self.mostrar_habilidad()}, y trabajo en: {self.empresa}')

roberto = Empleado('Roberto', 43, 'Mexico', 'Programador', 80000)

erick = EmpleadoArtista('Erick', 43, 'Mexico', 'Cantar', '1200', 'Bimbo')
erick.presentarse()

herencia = issubclass(Empleado, Persona)
print(herencia)

instancia = isinstance(erick, Persona)
print(instancia)