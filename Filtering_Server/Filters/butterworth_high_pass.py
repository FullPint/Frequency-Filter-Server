import numpy as np
from .butterworth_low_pass import ButterWorthLowPass

class ButterWorthHighPass(ButterWorthLowPass):
    def __init__(self, shape, cutoff, order):
        super().__init__(shape, cutoff, order)

    def build_filter(self):
        super().build_filter()
        self.mask = 1 - super().get_filter()
