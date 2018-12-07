import numpy as np
from .ideal_low_pass import IdealLowPass

class IdealHighPass(IdealLowPass):
    def __init__(self, shape, cutoff):
        super().__init__(shape, cutoff)

    def build_filter(self):
        super().build_filter()
        self.mask = 1 - super().get_filter()
