from habitos import Habitos

def guardar_elementos():
    try:
        guardar = {}

        numero = int(input('Introduce cuántos hábitos deseas agregar: '))

        for _ in range(numero):
            habito = Habitos()
            habito.agregar_elementos()
            guardar[habito._nombre] = habito

        return guardar

    except ValueError:
        print('Por favor, introduce una opción válida.')

def mostrar_habitos_guardados(habitos):
    for nombre, habito in habitos.items():
        print(habito.mostrar_informacion())

if __name__ == "__main__":
    habitos_guardados = guardar_elementos()
    if habitos_guardados:
        mostrar_habitos_guardados(habitos_guardados)
