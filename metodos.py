class Celular:
    # Atributos de instancia

    def __init__(self, marca, modelo, camara):   # Constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Metodos

    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo} ')
    def cortar(self):
        print(f'Cortaste la llamada desde un: {self.modelo}')

celular_1 = Celular('Samsung','S23', '48MP')
celular_2 = Celular('Apple', 'iPhone 15', '48MP')

celular_1.llamar()
celular_2.cortar()
