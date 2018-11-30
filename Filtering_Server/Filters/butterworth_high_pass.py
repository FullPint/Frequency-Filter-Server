import numpy as np
from .filter import Filter
from .butterworth_low_pass import ButterWorthLowPass

class ButterWorthHighPass(ButterWorthLowPass, Filter):
    def __init__(self, shape, cutoff, order):
        super().__init__(shape, cutoff, order)
        self.filter = 1 - super().build_filter()
