import numpy as np
from .filter import Filter

class IdealLowPass(Filter):
    def __init__(self, shape, cutoff):
        super().__init__(shape)
        self.cutoff = cutoff

    def build_filter(self):
        filter = np.zeroes((self.p, self.q))
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            filter[u][v] = 1 if self.calculate_distance(u, v) > self.cutoff else 0
            index_iterator.iternext()
        return filter

    def calculate_distance(self, u, v):
        dist = np.sqrt(np.square(u - (self.p/2)) + np.square(v - (self.q/2)))
        return dist
