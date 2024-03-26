class Animal:
    def comer(self):
        print('El animal esta comiendo')

class Ave(Animal):
    def volar(self):
        print('El animal esta volando')

class Mamifero(Animal):
    def amamantar(self):
        print('El animal esta amamantando')

class Murcielago(Mamifero, Ave):
    pass

ave = Ave()

ave.volar()
ave.comer()
print(Ave.mro())