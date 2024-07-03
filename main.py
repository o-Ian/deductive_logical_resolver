from gridSolver.Grid import Grid
from gridRecognition.GridRecognitionService import GridRecognitionService
from gridSolver.GridSolverService import GridSolverService

possible_elements_5 = ['circle', 'plus', 'square', 'triangle', 'star']
possible_elements_4 = ['circle', 'plus', 'square', 'triangle']
possible_elements_3 = ['plus', 'circle', 'triangle']

# Instantiating Services Objects
gridRecognitionService = GridRecognitionService()
gridSolverService = GridSolverService()

img_path = gridRecognitionService.get_last_accessed_file('/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/infFiles/entire_grids');
folder_symbols = "/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/infFiles/specific_symbols"

# Number of columns and rows of grid (if it's a square)
matriz = 5

if (matriz == 5):
    grid_size = (5, 5)
    possible_elements_default = possible_elements_5
elif (matriz == 4):
    grid_size = (4, 4)
    possible_elements_default = possible_elements_4
elif (matriz == 3):
    grid_size = (3, 3)
    possible_elements_default = possible_elements_3

# If your grid size was not taken into account, personalize your own value
# grid_size = (row_number, column_number)
# possible_elements_default = possible_elements_x

# Create an image for each grid element
create_grid = gridRecognitionService.crop_grid(img_path, grid_size)

# Check all the created grid elements and applies the recognize model
initial_matriz = gridRecognitionService.applyModel(folder_symbols, grid_size)

# Solving sudoku
gridEntity = Grid(initial_matriz, possible_elements_default)
resolved_grid = gridSolverService.fillGrid(gridEntity)

print(f'The grid image used was: {img_path}')

for rows in resolved_grid:
    print(rows)

if(gridEntity.question_mark_position):
    print(f'The answer is: {resolved_grid[gridEntity.question_mark_position[0]][gridEntity.question_mark_position[1]]}')
