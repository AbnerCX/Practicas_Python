class Mascota:
    def __init__(self, nombre, especie):
        self._nombre = nombre
        self._especie = especie

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_especie(self):
        return self._especie

    def set_especie(self, especie):
        self._especie = especie


class MascotaConEdad(Mascota):
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie)
        self._edad = edad

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad


class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio


class ProductoConDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self._descuento = descuento

    def get_descuento(self):
        return self._descuento

    def set_descuento(self, descuento):
        self._descuento = descuento

    def calcular_precio_con_descuento(self):
        return self._precio * (1 - self._descuento)


class Libro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor


class LibroConISBN(Libro):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo, autor)
        self._isbn = isbn

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn


# Ejemplo de uso:
mascota = MascotaConEdad("Firulais", "Perro", 5)
print(mascota.get_nombre())
print(mascota.get_especie())
print(mascota.get_edad())
mascota.set_nombre("Rex")
mascota.set_especie("Gato")
mascota.set_edad(3)
print(mascota.get_nombre())
print(mascota.get_especie())
print(mascota.get_edad())

producto = ProductoConDescuento("Camiseta", 20, 0.1)
print(producto.get_nombre())
print(producto.get_precio())
print(producto.get_descuento())
print(producto.calcular_precio_con_descuento())

libro = LibroConISBN("Python Programming", "John Doe", "978-1-0000-0000-1")
print(libro.get_titulo())
print(libro.get_autor())
print(libro.get_isbn())
libro.set_titulo("Learning Python")
libro.set_autor("Jane Smith")
libro.set_isbn("978-1-1111-1111-1")
print(libro.get_titulo())
print(libro.get_autor())
print(libro.get_isbn())
