from numpy import np

class Filter:
    def __init__(self, shape):
        self.shape = shape
        self.p = shape[0]
        self.q = shape[1]
        self.filter = self.build_filter()

    def build_filter(self):
        return np.zeros(self.shape)

    def get_filter(self):
        return self.filter

    def calculate_distance(self, u, v):
        return np.sqrt((u - (self.p/ 2)) ** 2 + ((v - (self.q / 2)) ** 2))
