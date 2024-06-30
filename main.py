from Grid import Grid
from gridRecognition.cropImage import crop_grid
from gridRecognition.applyModel import applyModel


possible_elements_5 = ['circle', 'plus', 'square', 'triangle', 'star']
possible_elements_4 = ['circle', 'plus', 'square', 'triangle']

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
img_path = "/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/infFiles/grid_image.png"
folder_symbols = "/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/infFiles/test"
grid_size = (5,5)

#Cria uma imagem pra cada elemento do grid
create_crid = crop_grid(img_path, grid_size)

#Olha os arquivos dentro do folder e aplica o modelo de reconhecimento
matriz_inicial = applyModel(folder_symbols, grid_size)

#Resolver matriz
gridClass = Grid(matriz_inicial, possible_elements_5)

gridClass.fillGrid()

print(gridClass.question_mark_position)
for rows in gridClass.grid:
    print(rows)
print(f'A resposta é: {gridClass.grid[gridClass.question_mark_position[0]][gridClass.question_mark_position[1]]}')