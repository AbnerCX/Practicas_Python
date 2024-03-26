class MiClase:
    def __init__(self):
        self._atributo_privado = 'Valor' #El guion bajo significa que es privado
        self.__atributo_privado = 'Valor'  #el doble guion es muy muy privado

    def __hablar(self):
        print('Hola como estas')

objeto = MiClase()
print(objeto.__hablar())
