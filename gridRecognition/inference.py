import pickle

from img2vec_pytorch import Img2Vec
from PIL import Image

def inference(image_path):
    with open('/Users/ian/IdeaProjects/Preenchedora_matriz/gridRecognition/model/model.p', 'rb') as f:
        model = pickle.load(f)

    img2vec = Img2Vec()

    img = Image.open(image_path).convert('RGB')

    features = img2vec.get_vec(img)

    pred = model.predict([features])

    return(pred)