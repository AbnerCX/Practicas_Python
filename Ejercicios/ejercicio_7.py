class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def mostrar_datos(self):
        print(f''' 
        --EMPLEADO--
        Nombre: {self.nombre}
        Edad: {self.edad}
        Salario: {self.salario}
        
        ''')

class Desarollador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje, horas):
       super().__init__(nombre, edad, salario)
       self.lenguaje = lenguaje
       self.horas = horas

    def mostrar_datos(self):
        print(f''' 
        --EMPLEADO--
        Nombre: {self.nombre}
        Edad: {self.edad}
        Salario: {self.salario}
        Lenguajes: {self.lenguaje}
        Horas extras: {self.horas}
        
        ''')


empleado_1 = Empleado('Eduardo', 35, 5600)
empleado_1.mostrar_datos()

desarollador_1 = Desarollador('Abner', 21, 6500, 'Python y C++', 45)
desarollador_1.mostrar_datos()
