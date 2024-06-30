from PIL import Image

def crop_grid(image_path, grid_size):
    img = Image.open(image_path)
    width, height = img.size
    cell_width, cell_height = width // grid_size[1], height // grid_size[0]
    c = 0
    cropped_cells = []
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            left = col * cell_width
            top = row * cell_height
            right = left + cell_width
            bottom = top + cell_height
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(f"/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/infFiles/test/{row}_{col}.png")
            cropped_cells.append(cropped_img)
            c +=1

    return cropped_cells