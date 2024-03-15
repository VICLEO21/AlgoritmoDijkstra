def printDicc(dicc):
    for i in dicc:
        print(f'Vertice: {i}')
        for j in dicc[i]:
            print(F'\tRel: {j} \n\t\tPeso: {dicc[i][j]}')
    return ''