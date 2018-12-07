import numpy as np
from .filter import Filter

class Laplace(Filter):
    def __init__(self, shape):
        super().__init__(shape)

    def build_filter(self):
        mask = np.zeros(self.shape)
        index_iterator = np.nditer(mask, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            mask[u][v] = -(np.square(u - np.divide(self.p, 2)) + np.square(v - np.divide(self.q, 2)))
            index_iterator.iternext()
        self.mask = mask
