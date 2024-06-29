from Grid import Grid

possible_elements_5x5 = ['1', '2', '3', '4', '5']
possible_elements__4x4 = ['1', '2', '3', '4']

matriz_5x5= [
    ['1', '2', '-', '-', '-'],
    ['2', '-', '-', '-', '-'],
    ['-', '-', '1', '-', '-'],
    ['-', '1', '-', '-', '-'],
    ['-', '-', '-', '-', '1']
]

matriz_4x4= [
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
]

gridClass = Grid(matriz_5x5, possible_elements_5x5)
result =  gridClass.fillGrid()

for result_linha in result:
    print(result_linha)