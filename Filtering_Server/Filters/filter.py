from numpy import np

class Filter:
    def __init__(self, shape):
        self.shape = shape
        self.filter = self.build_filter()

    def build_filter(self):
        self.filter = np.zeros(shape)

    def get_filter(self):
        return self.filter
