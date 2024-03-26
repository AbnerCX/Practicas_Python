class Celular:
    # Atributos de instancia

    def __init__(self, marca, modelo, camara):   # Constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular_1 = Celular('Samsung','S23', '48MP')
celular_2 = Celular('Apple', 'iPhone 15', '48MP')

print(celular_1.marca)
print(celular_2.marca)