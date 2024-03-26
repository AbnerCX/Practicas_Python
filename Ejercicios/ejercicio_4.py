class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacion(self):
        print(f'''
        ---Informacion del libro---
        Nombre: {self.titulo}
        Autor: {self.autor}
        Paginas: {self.paginas}
        
        ''')

class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def mostrar_libros(self):
        for libros in self.lista_libros:
            libros.informacion()


biblioteca = Biblioteca()

libro_1 = Libro('Alicia', 'Pedro Roiter', 445)
libro_2 = Libro("1984", "George Orwell", 328)

biblioteca.agregar_libro(libro_1)
biblioteca.agregar_libro(libro_2)
biblioteca.mostrar_libros()
