class Celular():
    # Atributos estaticos

    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

celular_1 = Celular()
celular_2 = Celular()

print(celular_1.marca,celular_1.modelo,celular_1.camara)

celular_2.marca = 'Apple'
celular_2.modelo = 'iPhone 15'

print(celular_2.marca,celular_2.modelo,celular_2.camara)