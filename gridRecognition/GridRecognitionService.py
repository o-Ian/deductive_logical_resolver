import os
from PIL import Image
import pickle
from img2vec_pytorch import Img2Vec

class GridRecognitionService:
    def get_last_accessed_file(self, folder_path):

        last_accessed_time = 0
        last_accessed_file = None

        for filename in os.listdir(folder_path):
            if(filename != '.gitkeep'):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    access_time = os.path.getmtime(filepath)
                    if access_time > last_accessed_time:
                        last_accessed_time = access_time
                        last_accessed_file = filepath

        return last_accessed_file

    def delete_files_in_directory(self, directory_path):
        files = os.listdir(directory_path)
        for file in files:
            if(file != '.gitkeep'):
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    def crop_grid(self, image_path, grid_size):
        img = Image.open(image_path)
        width, height = img.size
        cell_width, cell_height = width // grid_size[1], height // grid_size[0]
        c = 0
        cropped_cells = []
        folder_path = '/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/infFiles/specific_symbols'

        self.delete_files_in_directory(folder_path)

        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                left = col * cell_width
                top = row * cell_height
                right = left + cell_width
                bottom = top + cell_height
                cropped_img = img.crop((left, top, right, bottom))
                cropped_img.save(f"{folder_path}/{row}_{col}.png")
                cropped_cells.append(cropped_img)
                c +=1

        return cropped_cells

    def createEmptyGrid(self, grid_size: tuple):
        grid = []
        for _ in range(grid_size[0]):
            row = []
            for _ in range(grid_size[1]):
                row.append("-")
            grid.append(row)
        return grid

    def inference(self, image_path):
        with open('/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/model/model.p', 'rb') as f:
            model = pickle.load(f)

        img2vec = Img2Vec()

        img = Image.open(image_path).convert('RGB')

        features = img2vec.get_vec(img)

        pred = model.predict([features])

        return(pred)

    def applyModel(self, folder_name, grid_size):
        matriz = self.createEmptyGrid(grid_size)
        for file in os.listdir(folder_name):
            if(file != '.gitkeep'):
                symbol = self.inference(f'{folder_name}/{file}')
                file_name = file.replace('.png', '')
                file_row = int(file_name.split('_')[0])
                file_column = int(file_name.split('_')[1])
                matriz[file_row][file_column] = symbol[0]
        return matriz