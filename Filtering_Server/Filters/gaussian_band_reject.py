import numpy as np
from .filter import Filter

class GaussianBandReject(Filter):
    def __init__(self, shape):
        Filter.__init__(self, shape)
