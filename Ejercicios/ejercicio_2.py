class Libro:

    def __init__(self, titulo, autor, paginas, genero):

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero

    def informacion(self):
        print(f"""
        ---Informacion del libro---
        Titulo del libro: {self.titulo}
        Autor: {self.autor}
        Paginas del libro: {self.paginas} 
        Genero: {self.genero} 
        """)

libro_1 = Libro('Alicia en el pais de las maravillas', 'Maragira', 455, 'Literario')
libro_2 = Libro('Dune', 'Frank', 543, 'Ciencia ficcion')
libro_3 = Libro('Hollow Knight', 'Team Cherry', 234, 'Ciencia ficcion')

libro_1.informacion()
libro_2.informacion()
libro_3.informacion()