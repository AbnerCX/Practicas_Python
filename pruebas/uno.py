arreglo = [1,2,3,4,5,6,7,8,9,10]

def recorrer_arreglo_todos_los_elementos(arreglo):
    for x in range(len(arreglo)):
        print(f"Indice: {x} Valor: {arreglo[x]}")


def recorrer_arreglo_para_comparar_elementos(arreglo):
    for x in range(len(arreglo) - 1):
        if arreglo[x] < arreglo[x + 1]:
            print(f"{arreglo[x]} es menor que {arreglo[x + 1]}")
        else:
            print(f"{arreglo[x]} no es menor que {arreglo[x + 1]}")


recorrer_arreglo_todos_los_elementos(arreglo)
print("COMPARAR ELEMENTOS")
recorrer_arreglo_para_comparar_elementos(arreglo)