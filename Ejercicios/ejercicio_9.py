class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f'\n El nombre de tu personaje es: {self.nombre}')

class Habilidades:
    def __init__(self, tipo ,pasiva, especial):
        self.tipo = tipo
        self.pasiva = pasiva
        self.especial = especial

    def mostrar_habilidades(self):
        print(f'''
        
        Tipo de habilidad: {self.tipo}
        Habilidad pasiva: {self.pasiva}
        Habilidad especial: {self.especial}

        ''')

class Faccion:
    def __init__(self, nombre_faccion, lider, habilidad_especial, enemigos):
        self.nombre_faccion = nombre_faccion
        self.lider = lider
        self.habilidad_especial = habilidad_especial
        self.enemigos = enemigos

    def mostrar_facciones(self):
        print(f'''
        Nombre de la faccion: {self.nombre_faccion}
        Lider de la faccion: {self.lider}
        Habilidad especial de faccion: {self.habilidad_especial}
        Enemigos de la faccion: {self.enemigos}
        ''')

class Humanos(Personaje, Habilidades, Faccion):
    def __init__(self, nombre, tipo ,pasiva, especial, nombre_faccion, lider, habilidad_especial, enemigos):
        Personaje.__init__(self, nombre)
        Habilidades.__init__(self, tipo,pasiva,especial)
        Faccion.__init__(self, nombre_faccion,lider,habilidad_especial,enemigos)

humanos = Humanos('John', 'Basica', 'Sin pasiva', 'Sin especial', 'Humanidad', 'El emperador', 'Sin habilidad', 'Orkos')
humanos.mostrar_nombre()
humanos.mostrar_habilidades()
humanos.mostrar_facciones()