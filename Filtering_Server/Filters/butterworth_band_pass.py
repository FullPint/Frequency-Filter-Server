import numpy as np
from .filter import Filter

class ButterWorthBandPass(Filter):
    def __init__(self, shape):
        Filter.__init__(self, shape)
