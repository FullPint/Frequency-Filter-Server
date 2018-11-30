import numpy as np
from .filter import Filter

class Laplace(Filter):
    def __init__(self, shape):
        super().__init__(shape)

    def build_filter(self):
        filter = np.zeros(self.shape)
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            filter[u][v] = 1 + (np.square(u - self.p) + np.square(v - self.q))
            index_iterator.iternext()
        return filter
