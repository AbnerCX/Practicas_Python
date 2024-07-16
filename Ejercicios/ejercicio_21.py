class Automovil:
    def __init__(self, year = None, color=None, modelo = None, marca = None):
        self.__color = color
        self.__modelo = modelo
        self.__marca = marca
        self.__year = year

    def mostrar_informacion(self):
        print(f'''
        Marca: {self.__marca}
        Modelo: {self.__modelo}
        Color: {self.__color}
        Year: {self.__year}
        ''')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,marca):
        self.__marca = marca

    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

    def establecer_valores(self):
        self.__marca = input('Introduce la marca del vehiculo: ')
        self.__modelo = input('Introduce el modelo del vehiculo: ')
        self.__color = input('Introduce el color del vehiculo: ')


carro = Automovil()
carro.setYear('1999')
carro.mostrar_informacion()
carro.establecer_valores()
print(carro.marca)
carro.mostrar_informacion()