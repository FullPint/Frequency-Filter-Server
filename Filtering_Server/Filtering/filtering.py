import numpy as np
import Filtering_Server.Filters as Filters
from Filtering_Server.FFT import FFT_DIP
import uuid

class Filtering:
    def __init__(self, image, filter_name, cutoff=None, a_value = None, order = None, width = None, implementation = 'numpy'):
        self.id = uuid.uuid1()
        self.filter_name = filter_name
        self.image = image
        self.shape = image.shape
        self.filter_image = np.zeros(self.shape)
        self.filter_freq_image = np.zeros(self.shape)
        self.cutoff = cutoff
        self.a_value = a_value
        self.order = order
        self.width = width
        self.fft = FFT_DIP if implementation != 'numpy' else np.fft

    def get_filter(self):
        if self.filter_name == "butterworth_band_pass":
            filter = Filters.ButterWorthBandPass(self.shape, self.cutoff, self.order, self.width)
        elif self.filter_name == "butterworth_band_reject":
            filter = Filters.ButterWorthBandReject(self.shape, self.cutoff, self.order, self.width)
        elif self.filter_name == "butterworth_high_pass":
            filter = Filters.ButterWorthHighPass(self.shape, self.cutoff, self.order)
        elif self.filter_name == "butterworth_low_pass":
            filter = Filters.ButterWorthLowPass(self.shape, self.cutoff, self.order)
        elif self.filter_name == "gaussian_band_pass":
            filter = Filters.GaussianBandPass(self.shape, self.cutoff, self.width)
        elif self.filter_name == "gaussian_band_reject":
            filter = Filters.GaussianBandReject(self.shape, self.cutoff, self.width)
        elif self.filter_name == "gaussian_high_pass":
            filter = Filters.GaussianHighPass(self.shape, self.cutoff)
        elif self.filter_name == "gaussian_low_pass":
            filter = Filters.GaussianLowPass(self.shape, self.cutoff)
        elif self.filter_name == "high_boost":
            filter = Filters.HighBoost(self.shape, self.cutoff, self.a_value)
        elif self.filter_name == "ideal_band_pass":
            filter = Filters.IdealBandPass(self.shape, self.cutoff, self.width)
        elif self.filter_name == "ideal_band_reject":
            filter = Filters.IdealBandReject(self.shape, self.cutoff, self.width)
        elif self.filter_name == "ideal_high_pass":
            filter = Filters.IdealHighPass(self.shape, self.cutoff)
        elif self.filter_name == "ideal_low_pass":
            filter = Filters.IdealLowPass(self.shape, self.cutoff)
        elif self.filter_name == "laplacian_filter":
            filter = Filters.Laplace(self.shape)
        elif self.filter_name == "unsharp_mask":
            filter = Filters.UnsharpMask(self.shape, self.cutoff)
        else:
            filter = Filters.filter(self.shape)
        return filter

    def apply_filter(self):
        fft_image = np.fft.fft2(self.image)
        fft_image = np.fft.fftshift(fft_image)
        filter = self.get_filter()
        filter.build_filter()
        mask = filter.get_filter()
        fft_image = np.multiply(fft_image, mask)
        filter_freq_image = np.uint8(np.log(np.absolute(fft_image)) * 10)
        filter_image = np.fft.ifftshift(fft_image)
        filter_image = np.fft.ifft2(filter_image)
        filter_image = np.absolute(filter_image)
        filter_image = self.post_process_image(filter_image)

        self.filter_freq_image = filter_freq_image
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
        return stretch_image
