import numpy as np
from .filter import Filter

class IdealLowPass(Filter):
    def __init__(self, shape, cutoff):
        self.cutoff = cutoff
        super().__init__(shape)

    def build_filter(self):
        filter = np.zeros(self.shape)
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            filter[u][v] = 1 if super().calculate_distance(u, v) > self.cutoff else 0
            index_iterator.iternext()
        return filter
