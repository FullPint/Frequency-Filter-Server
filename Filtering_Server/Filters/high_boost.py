import numpy as np
from .filter import Filter
from .ideal_high_pass import IdealHighPass as HP

class HighBoost(Filter):
    def __init__(self, shape, cutoff, a):
        super().__init__(shape)
        self.cutoff = cutoff
        self.a = a

    def build_filter(self):
        hp = HP(self.shape, self.cutoff)
        hp.build_filter()
        self.mask = (self.a - 1) - hp.get_filter()
