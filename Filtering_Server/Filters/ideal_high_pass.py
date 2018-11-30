import numpy as np
from .filter import Filter
from .ideal_low_pass import IdealLowPass

class IdealHighPass(IdealLowPass, Filter):
    def __init__(self, shape, cutoff):
        super().__init__(shape, cutoff)
        self.filter = 1 - super().build_filter()
