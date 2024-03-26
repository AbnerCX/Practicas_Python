class ProductoElectronico:
    def __init__(self, nombre, precio, marca):

            self.nombre = nombre
            self.precio = precio
            self.marca = marca

    def mostrar_informacion(self):
        print(f'''
        ---Detalles del producto---
        Nombre: {self.nombre}
        Marca: {self.marca}
        Precio: {self.precio}
        
        ''')

class Telefono(ProductoElectronico):
    def __init__(self, nombre, precio, marca, modelo, pantalla):
        super().__init__(nombre, precio, marca)
        self.modelo = modelo
        self.pantalla = pantalla

    def mostrar_informacion(self):
        print(f'''
        ---Detalles del producto---
        Nombre: {self.nombre}
        Marca: {self.marca}
        Precio: {self.precio}
        Modelo: {self.modelo}
        Pantalla: {self.pantalla}
        ''')

class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, modelo, sistema):
        super().__init__(nombre, precio, marca)
        self.modelo = modelo
        self.sistema = sistema

    def  mostrar_informacion(self):
        print(f'''
        ---Detalles del producto---
        Nombre: {self.nombre}
        Marca: {self.marca}
        Precio: {self.precio}
        Modelo: {self.modelo}
        Sistema operativo: {self.sistema}
        ''')

class Tablet(ProductoElectronico):
    def __init__(self, nombre, precio, marca, modelo, conexion):
        super().__init__(nombre, precio, marca)
        self.modelo = modelo
        self.conexion = conexion

    def mostrar_informacion(self):
        print(f'''
        ---Detalles del producto---
        Nombre: {self.nombre}
        Marca: {self.marca}
        Precio: {self.precio}
        Modelo: {self.modelo}
        Conexion: {self.conexion}
        ''')

pc = ProductoElectronico('Razer PC', 45000, 'Razer')
pc.mostrar_informacion()

celular = Telefono('iPhone', 30600, 'Apple', 'iPhone 15', '9 pulgadas')
celular.mostrar_informacion()

lap = Laptop('Realme 8', 15000, 'HP', 'NVME15', 'Windows')
lap.mostrar_informacion()

tables = Tablet('Idepad', 2345, 'Samsung', 'Honor 3', 'WiFi 4G')
tables.mostrar_informacion()