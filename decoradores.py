def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print('Vamos a realizar una operacion')

        funcion_parametro()

        print('Hemos terminado el calculo')
        print('\n')
    return funcion_interior


@funcion_decoradora
def suma():
    print(25+25)

@funcion_decoradora
def resta():
    print(25-20)

suma()
resta()