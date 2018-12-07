import numpy as np
from .gaussian_low_pass import GaussianLowPass

class GaussianHighPass(GaussianLowPass):
    def __init__(self, shape, cutoff):
        super().__init__(shape, cutoff)

    def build_filter(self):
        super().build_filter()
        self.mask = 1 - super().get_filter()
