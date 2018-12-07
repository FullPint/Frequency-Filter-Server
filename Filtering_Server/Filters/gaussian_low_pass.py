import numpy as np
from .filter import Filter

class GaussianLowPass(Filter):
    def __init__(self, shape, cutoff):
        super().__init__(shape)
        self.cutoff = cutoff

    def build_filter(self):
        mask = np.zeros(self.shape)
        index_iterator = np.nditer(mask, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            distance = super().calculate_distance(u, v)
            mask[u][v] =  1 / np.exp((distance * distance) / (2 * self.cutoff * self.cutoff))
            index_iterator.iternext()
        self.mask = mask
