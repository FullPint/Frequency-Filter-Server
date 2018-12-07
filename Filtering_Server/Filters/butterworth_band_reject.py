import numpy as np
from .butterworth_band_pass import ButterWorthBandPass

class ButterWorthBandReject(ButterWorthBandPass):
    def __init__(self, shape, cutoff, order, width):
        super().__init__(shape, cutoff, order, width)

    def build_filter(self):
        super().build_filter()
        self.mask = 1 - super().get_filter()
