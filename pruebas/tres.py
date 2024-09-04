def solution(statues):

    statues.sort()
    cont = 0
    
    for x in range(statues[0], statues[-1] + 1):
        if x not in statues:
            cont += 1

    return cont


lista = [2, 10]

print(solution(lista))