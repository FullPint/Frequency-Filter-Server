import numpy as np
from .ideal_band_pass import IdealBandPass

class IdealBandReject(IdealBandPass):
    def __init__(self, shape, cutoff, width):
        super().__init__(shape, cutoff, width)

    def build_filter(self):
        super().build_filter()
        self.mask = 1 - super().get_filter()
