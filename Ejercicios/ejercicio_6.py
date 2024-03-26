class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def informacion(self):

        print(f'''
        ---Lista de productos---
        Nombre: {self.nombre}
        Precio: {self.precio} pesos.
        Cantidad: {self.cantidad} piezas.
        ''')

class Inverntario:
    def __init__(self):
        self.producto = []

    def agregar_producto(self, producto):
        self.producto.append(producto)

    def mostrar_informacion(self):
        for product in self.producto:
            product.informacion()

producto_1 = Producto('Mr.Musculo', 35, 65)
producto_2 = Producto('Ace', 25, 76)
inventario_1 = Inverntario()

inventario_1.agregar_producto(producto_2)
inventario_1.agregar_producto(producto_1)
inventario_1.mostrar_informacion()

#producto_1.informacion()