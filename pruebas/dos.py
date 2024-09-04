def imprimir_elemento_y_indice(array):
    for x in range(len(array)):
        print(f"Indice: {x} --- Elemento: {array[x]}")

def imprimir_maximo_y_minimo(array):        

    max_valor = array[0]
    min_valor = array[0]

    for x in range(1, len(array)):
        if array[x] > max_valor:
            max_valor = array[x]
        if array[x] < min_valor:
            min_valor = array[x]
    
    print(f"El valor mayor del array es: {max_valor}")
    print(f"El valor mas pequeño del array es: {min_valor}")


def imprimir_max_valor_optimizado(array):
    max_valor = print(max(array))
    min_valr = print(min(array))


def comparar_elementos_consecutivos(array):

    for x in range(len(array) - 1):
        if array[x] < array[x + 1]:
            print(f"El valor de {array[x]} es [menor] que {array[x + 1]}")
        else:
            print(f"El valor de {array[x]} es [mayor] que {array[x + 1]}")


def contar_numeros_negativos(array):
    cantidad = 0

    for x in range(len(array)):
        if array[x] < 0:
            cantidad += 1

    print(cantidad)

def menu():
    array = [3, -1, 4, 7, 9, -5, 8, -2, 12, 6, 0, -8, 11, 10, -4]

    while True:
        
        print("\nSelecciona la opcion que deseas ejecutar:")
        print("1. Imprimir elementos y sus indices")
        print("2. Imprimir valor maximo y minimo")
        print("3. Imprimir valor maximo y minimo (optimizado)")
        print("4. Comparar elementos consecutivos")
        print("5. Contar numeros negativos")
        print("6. Salir")

        opcion = int(input("Introduce el numero de la opcion: "))

        if opcion == 1:
            imprimir_elemento_y_indice(array)
        elif opcion == 2:
            imprimir_maximo_y_minimo(array)
        elif opcion == 3:
            imprimir_max_valor_optimizado(array)
        elif opcion == 4:
            comparar_elementos_consecutivos(array)
        elif opcion == 5:
            contar_numeros_negativos(array)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor, selecciona una opcion del 1 al 6.")

if __name__ == "__main__":
    menu()