from Auto import Auto

class AutoElectrico(Auto):
    def __init__(self, marca, modelo, autonomia, duracion_bateria):
        super().__init__(marca, modelo, autonomia)
        self.__duracion_bateria = duracion_bateria

    @property
    def duracion_bateria(self):
        return self.__duracion_bateria

    @duracion_bateria.setter
    def duracion_bateria(self, duracion_bateria):
        self.__duracion_bateria = duracion_bateria

    def __mostrar_informacion(self):
        print(f'''
        Marca: {self.marca}
        Modelo: {self.modelo}
        Autonomia: {self.autonomia}      
        Duracion de la bateria: {self.duracion_bateria} horas
        ''')

    def mostrar_info(self):
        self.__mostrar_informacion()