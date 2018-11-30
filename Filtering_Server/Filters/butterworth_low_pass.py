import numpy as np
from .filter import Filter

class ButterWorthLowPass(Filter):
    def __init__(self, shape, cutoff, order):
        self.cutoff = cutoff
        self.order = order
        super().__init__(shape)

    def build_filter(self):
        filter = np.zeros(self.shape)
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            distance = self.calculate_distance(u, v)
            filter[u][v] = 1 / (1 + ((distance / self.cutoff) ** (2 * self.order)))
            index_iterator.iternext()
        return filter
