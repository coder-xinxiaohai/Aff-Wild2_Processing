import torch
import pickle
import numpy as np

from PIL import Image
from torch.utils.data import Dataset


class Affwild2_annotation(object):
    """A class that represents a sample from Aff-Wild2."""

    def __init__(self, frame_path, expression, valence, arousal):
        super(Affwild2_annotation, self).__init__()
        self.frame_path = frame_path
        self.expression = expression
        self.valence = valence
        self.arousal = arousal


class Affwild2_dataset(Dataset):
    """Aff-Wild2"""

    def __init__(self, data_pkl, emb_pkl, train=True, transform=None):

        self.train = train
        self.transform = transform

        data_pickle = pickle.load(open(data_pkl, 'rb'))
        if train:
            self.data = data_pickle['train']
        else:
            self.data = data_pickle['val']

        self.inp = torch.load(emb_pkl)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        sample = self.data[idx]
        img_name = sample.frame_path
        image = Image.open(img_name).convert("RGB")

        expression = sample.expression
        if self.transform:
            image = self.transform(image)

        cont = np.array([sample.valence, sample.arousal])

        return image, expression, cont, self.inp
