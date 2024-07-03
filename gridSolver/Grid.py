import copy
import random


class Grid:

    def __init__(self, grid, possible_elements, question_mark_position=False):
        self.grid = grid
        self.old_grid = grid
        self.possible_elements = possible_elements

    def fillGrid(self):
        c = 0
        while True:
            fake_grid = copy.deepcopy(self.grid)
            c += 1
            print('#######################')
            print(f'Attempt number: {c}')
            for cont_linha, linha in enumerate(fake_grid):
                for cont_coluna, symbol in enumerate(linha):
                    if symbol == 'empty' or symbol == 'question_mark':
                        if symbol == 'question_mark':
                            self.question_mark_position = (cont_linha, cont_coluna)
                        possible_elements_2 = self.possible_elements.copy()
                        for available_symbol in self.possible_elements:
                            if available_symbol in linha:
                                possible_elements_2.remove(available_symbol)
                        for linha2 in fake_grid:
                            if (linha2[cont_coluna] != 'empty' or linha2[cont_coluna] != 'question_mark') and linha2[cont_coluna] in possible_elements_2:
                                possible_elements_2.remove(linha2[cont_coluna])
                        if possible_elements_2:
                            element_to_be_added = random.choice(possible_elements_2)
                            fake_grid[cont_linha][cont_coluna] = element_to_be_added

            if not self.is_grid_empty(fake_grid):
                self.grid = fake_grid
                return self.grid
                break
    def is_grid_empty(self, grid):
        is_matriz_empty = False
        for cont_linha, linha in enumerate(grid):
            for cont_coluna, symbol in enumerate(linha):
                if symbol == 'empty':
                    is_matriz_empty = True
        return is_matriz_empty