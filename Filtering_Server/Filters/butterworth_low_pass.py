import numpy as np
from .filter import Filter

class ButterWorthLowPass(Filter):
    def __init__(self, shape, cutoff, order):
        super().__init__(shape)
        self.cutoff = cutoff
        self.order = order

    def build_filter(self)
