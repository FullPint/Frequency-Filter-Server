import numpy as np
from .filter import Filter
from .ideal_high_pass import IdealHighPass as HP

class HighBoost:
    def __init__(self, shape, cutoff, A):
        self.shape = shape
        self.cutoff = cutoff
        self.A = A
        self.filter = self.build_filter()

    def build_filter(self):
        hp = HP(self.shape, self.cutoff)
        filter = (self.A - 1) + hp.get_hpfilter()
        return filter

    def get_high_boost(self):
        return self.filter
