import numpy as np
from .filter import Filter

class GaussianBandPass(Filter):
    def __init__(self, shape, cutoff, width):
        super().__init__(shape)
        self.cutoff = cuttoff
        self.width = width

    def build_filter(self):
        mask = np.zeros(self.shape)
        index_iterator = np.nditer(mask, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            distance = super().calculate_distance(u, v)
            if distance == 0:
                mask[u][v] = 0
            else:
                mask[u][v] =  1 - np.exp(-(((distance ** 2 - self.cutoff ** 2) / (distance * self.width)) ** 2))
            index_iterator.iternext()
        self.mask = mask
