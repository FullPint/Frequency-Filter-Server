from high_boost import HighBoost
from .filter import Filter

class UnsharpMask(HighBoost):
    def __init__(self, shape, cutoff):
        super().__init__(shape, cutoff, A=1)
