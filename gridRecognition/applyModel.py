import os
import pickle

from img2vec_pytorch import Img2Vec
from PIL import Image

def createGrid(grid_size: tuple):
    grid = []
    for _ in range(grid_size[0]):  # Itera sobre as linhas
        row = []
        for _ in range(grid_size[1]):  # Itera sobre as colunas
            row.append("-")
        grid.append(row)
    return grid

def inference(image_path):
    with open('/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/model/model.p', 'rb') as f:
        model = pickle.load(f)

    img2vec = Img2Vec()

    img = Image.open(image_path).convert('RGB')

    features = img2vec.get_vec(img)

    pred = model.predict([features])

    return(pred)

def applyModel(folder_name, grid_size):
    matriz = createGrid(grid_size)
    for file in os.listdir(folder_name):
        symbol = inference(f'{folder_name}/{file}')
        file_name = file.replace('.png', '')
        file_row = int(file_name.split('_')[0])
        file_column = int(file_name.split('_')[1])
        matriz[file_row][file_column] = symbol[0]
    return matriz