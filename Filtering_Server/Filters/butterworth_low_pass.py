import numpy as np
from .filter import Filter

class ButterWorthLowPass(Filter):
    def __init__(self, shape, cutoff, order):
        super().__init__(shape)
        self.cutoff = cutoff
        self.order = order

    def build_filter(self):
        mask = np.zeros(self.shape)
        index_iterator = np.nditer(mask, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            distance = super().calculate_distance(u, v)
            mask[u][v] = 1 / (1 + ((distance / self.cutoff) ** (2 * self.order)))
            index_iterator.iternext()
        self.mask = mask
