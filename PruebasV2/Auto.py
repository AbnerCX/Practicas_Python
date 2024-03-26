class Auto:
    def __init__(self, marca, modelo, autonomia):
        self.__marca = marca
        self.__modelo = modelo
        self.__autonomia = autonomia

    def __mostrar_informacion(self):
        print(f'''
        Marca: {self.__marca}
        Modelo: {self.__modelo}
        Autonomia: {self.__autonomia}        
        ''')

    def mostrar_info(self):
        self.__mostrar_informacion()

    @property
    def marca(self):  # Cambio de get_marca a marca
        return self.__marca

    @marca.setter  # Cambio de get_marca a marca
    def marca(self, marca):  # Cambio de set_marca a marca
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def autonomia(self):
        return self.__autonomia

    @autonomia.setter
    def autonomia(self, autonomia):
        self.__autonomia = autonomia
