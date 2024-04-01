class Console:
    def __init__(self, marca, color, almacenamiento, precio):
        self.marca = marca
        self.color = color
        self.almacenamiento = almacenamiento
        self.precio = precio

    def show_information(self):
        print(f'''INFORMACION
        Marca: {self.marca}
        Color: {self.color}
        Almacenamiento: {self.almacenamiento}
        Precio: {self.precio}
            ''')

class PlayStation(Console):
    def __init__(self, marca, color, almacenamiento, precio, mando):
        super().__init__(marca, color, almacenamiento, precio)
        self.mando = mando

    def juegos_exclusivos(self):
        print('PlayStation tiene juegos exclusivos.')

class Xbox(PlayStation):
    def __init__(self, marca, color, almacenamiento, precio, mando, baterias):
        super().__init__(marca, color, almacenamiento, precio, mando)
        self.baterias = baterias

    def las_baterias(self):
        print('Xbox necesita baterias en 2024.')


consola = Console('Pc', 'Negra', '256', '500 USD')
consola.show_information()

playstation = PlayStation('Pley', 'Blanco', '500', '600 USD', 'DualShock')
playstation.juegos_exclusivos()

xbox = Xbox('ecsbox', 'Negro', '500', '450', 'Xbox Controller', 'AAA')
xbox.las_baterias()