import datetime

class Habitos:
    def __init__(self, nombre=None, descripcion=None, frecuencia=None):
        self._nombre = nombre
        self._descripcion = descripcion
        self._frecuencia = frecuencia
        self._fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def agregar_elementos(self):
        self._nombre = input("Introduce el nombre de tu hábito: ").title()
        self._descripcion = input('Introduce una breve descripción de este hábito: ').title()
        self._frecuencia = input('Introduce la frecuencia con la que deseas realizar este hábito: ').title()

    def mostrar_informacion(self):
        return f"""
        Nombre del hábito: {self._nombre}
        Descripción: {self._descripcion}
        Frecuencia: {self._frecuencia}
        Fecha de creación: {self._fecha_creacion}
        """
