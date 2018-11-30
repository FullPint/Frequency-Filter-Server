import numpy as np
from .filter import Filter
from .ideal_high_pass import IdealHighPass as HP

class HighBoost(Filter):
    def __init__(self, shape, cutoff, A):
        self.cutoff = cutoff
        self.A = A
        super().__init__(shape)

    def build_filter(self):
        hp = HP(self.shape, self.cutoff)
        filter = (self.A - 1) + hp.get_hpfilter()
        return filter
