import numpy as np
from .filter import Filter

class IdealLowPass(Filter):
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
            if distance <= self.cutoff:
                mask[u][v] = 1
            else:
                mask[u][v] = 0
            index_iterator.iternext()
        self.mask = mask
