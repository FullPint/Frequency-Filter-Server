import numpy as np
from .filter import Filter

class GaussianLowPass(Filter):
    def __init__(self, shape, cutoff):
        super().__init__(shape)
        self.cutoff = cutoff
        self.h = shape[0]
        self.w = shape[1]

    def build_filter(self):
        filter = np.zeroes((self.shape))
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            distance = self.calculate_distance(u, v)
            filter[u][v] =  1 / np.exp((distance * distance) / (2 * cutoff * cutoff)
            index_iterator.iternext()
        return filter

    def calculate_distance(self, u, v):
        return np.sqrt((u - (self.h/ 2)) ** 2 + ((v - (self.w / 2)) ** 2))
