class Empleado:
    def __init__(self, nombre, apellido, edad, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cargo = cargo

    def informacion(self):
        print(f'''
        ---Informacion del empleado---
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Edad: {self.edad}
        Cargo: {self.cargo}
        ''')

class RegistroEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def empleados_registrados(self):
        for empleado in self.empleados:
            empleado.informacion()

    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                print(f'El empleado {nombre} está registrado.')
                return
        print('El empleado no está registrado.')

empleado_1 = Empleado('Abner', 'Arce', 35, 'Gerente')
empleado_2 = Empleado('Abisai', 'Arce', 23, 'Practicante')

registro = RegistroEmpleados()
registro.agregar_empleado(empleado_1)
registro.agregar_empleado(empleado_2)


registro.buscar_empleado('Abner')

registro.empleados_registrados()