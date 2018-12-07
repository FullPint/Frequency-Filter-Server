import numpy as np
from .gaussian_band_pass import GaussianBandPass

class GaussianBandReject(GaussianBandPass):
    def __init__(self, shape, cutoff, width):
        super().__init__(shape, cutoff, width)

    def build_filter(self):
        super().build_filter()
        self.mask = 1 - super().get_filter()
