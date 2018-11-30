import numpy as np
import Filtering_Server.Filters as Filters
from Filtering_Server.FFT.fft import FFT_DIP

class Filtering:
    def __init__(self, filter_name, image, cutoff=None, order=None, implemntation='numpy'):
        self.filter_name = filter_name
        self.img = img
        self.shape = self.img.shape
        self.filter_image = np.zeros(self.shape)
        self.filter_freq_image = np.zeros(self.shape)
        self.cutoff = cutoff
        self.order = order
        self.fft = FFT_DIP if implemntation != 'numpy' else np.fft

    def get_filter(self):
        if self.filter_name == "buttertworth_high_pass":
            filter = Filters.ButterWorthHighPass(self.shape, self.cutoff, self.order)
        elif self.filter_name == "butterworth_low_pass":
            filter = Filters.ButterWorthLowPass(self.shape, self.cutoff, self.order)
        elif self.filter_name == "gaussian_high_pass":
            filter = Filters.GaussiaHighPass(self.shape, self.cutoff)
        elif self.filter_name == "gaussian_low_pass":
            filter = Filters.GaussianLowPass(self.shape, self.cutoff)
        elif self.filter_name == "high_boost":
            filter = Filters.HighBoost(self.shape, self.cutoff, self.A)
        elif self.filter_name == "ideal_high_pass":
            filter = Filters.IdealHighPass(self.shape, self.cutoff)
        elif self.filter_name == "ideal_low_pass":
            filter = Filters.IdealLowPass(self.shape, self.cutoff)
        elif self.filter_name == "laplacian_filter":
            filter = Filter.Laplace(self.shape)
        elif self.filter_name == "unsharp_mask":
            filter = Filters.UnsharpMask(self.shape)
        else:
            filter = Filters.filter(self.shape)
        return filter

    def apply_filter(self):
        fft_image = self.fft.fftshift(self.image)
        fft_image = self.fft.fft2(fft_image)
        filter = self.get_filter()
        filter_freq_image = np.multiply(fft_image, filter)
        self.filter_freq_image = np.uint8(np.log(np.absolute(filter_freq_image)) * 10)
        filter_image = np.fft.ifftshift(filter_freq_image)
        filter_image = np.fft.ifft2(filter_image)
        filter_image = np.absolute(filter_image)
        filter_image = post_process_image(filter_image)
        self.filter_image = filter_image

    def post_process_image(self, image):
        c_min = np.min(image)
        c_max = np.max(image)
        new_min = 0
        new_max = 255
        stretch_image = np.zeros((np.shape(image)), dtype=np.uint8)
        index_iterator = np.nditer(stretch_image, flags=['multi_index'])
        while not index_iterator.finished:
            i = index_iterator.multi_index[0]
            j = index_iterator.multi_index[1]
            stretch_image[i][j] = (image[i][j] - c_min) * ((new_max - new_min) / (c_max - c_min)) + new_min
            index_iterator.iternext()
        self.filter_image = stretch_image
