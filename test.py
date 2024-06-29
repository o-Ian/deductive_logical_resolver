import copy
import random


class Grid:
    def __init__(self, grid, possible_elements):
        self.grid = grid  # Agora são variáveis de instância
        self.old_grid = grid
        self.possible_elements = possible_elements

    def fillGrid(self):

    def is_grid_empty(self, grid):
    # ... (o resto do código do método is_grid_empty permanece igual)


# Exemplo de uso:
matriz_5x5 = [["-" for _ in range(5)] for _ in range(5)]
possible_elements_5x5 = ["A", "B", "C", "D", "E"]
gridClass = Grid(matriz_5x5, possible_elements_5x5)  # Cria uma instância de Grid

# Agora você pode usar os métodos da instância:
gridClass.fillGrid()
