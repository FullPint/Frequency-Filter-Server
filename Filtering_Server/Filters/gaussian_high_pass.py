import numpy as np
from .filter import Filter
from .gaussian_low_pass import GaussianLowPass

class GaussianHighPass(GaussianLowPass, Filter):
    def __init__(self, shape, cutoff):
        super().__init__(shape, cutoff)
        self.filter = 1 - self.build_filter()