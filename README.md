# Team B5 Report


## Run Filtering Server
```
  $conda env create -f environment.yml

  $conda activate filtering_server-dev

  $export FLASK_APP=Filtering_Server

  $export FLASK_ENV=development

  $flask run
```

## Objectives
Our objectives for this project were primarily to compute the DFT of an image in an efficient manner. The efficiency of this process is important because the DFT we compute is integral to the image processing component of the application.

We implemented the following filters as part of the image processing component:
* Ideal (Low/High) Pass
  * Ideal Band (Pass/Reject) Filters
* Butterworth (Low/High) Pass
  * Butterworth Band (Pass/Reject) Filters
* Gaussian (Low/High) Pass
  * Gaussian Band (Pass/Reject) Filters
* Laplacian Filter
* High Boost Filter
* Unsharp Mask Filter

In the next section, we will provide results of these filters along with a small explanation of the processing method.

## Filters

We'll be using the ubiquitous *Lenna* image, found everywhere throughout the field of Image Processing, for our comparisons:

![Lenna](report/images/Lenna.png)

While it doesn't affect the results, the following images will be generated with the Numpy method FFT method instead of the Team B5 method.

### Smoothing Frequency Filters

#### Ideal Lowpass
The ideal lowpass filter is the simplest lowpass filter; it essentially "cuts off" all components of the Fourier transform that are higher than a certain cutoff. This cutoff is the distance from the origin of the Fourier transformed image.

![Lenna | Ideal Lowpass Filter with cutoff of 20 versus a cutoff of 100](report/images/Lenna_ilp_20v100.png)

*Ideal lowpass filter applied to Lenna.png. On the left is a cutoff of 20, and on the right is a cutoff of 100. Note the "ring" effect visible on both images.*

#### Butterworth Lowpass
The Butterworth lowpass filter is different from the ideal lowpass filter in that it does not have a sharp cutoff value, but instead smoothly transitions between high and low frequencies. A Butterworth lowpass filter with a higher order will produce an image with 'more' lowpass filtering but also will exhibit much more ringing. An order of 2 is usually considered acceptable for most purposes, as it produces a good compromise between lowpass filtering and reducing ringing.

![Lenna | Butterworth Lowpass Filter with order of 2 and cutoff of 20 versus order of 2 and cutoff of 100](report/images/Lenna_blp_o2_20v100.png)

*Butterworth lowpass filter applied to Lenna.png. On the left is a cutoff of 20 and on the right is a cutoff of 100. Both images have an order of 2.*

#### Gaussian Lowpass


### Sharpening Frequency Filters

#### Ideal Highpass


#### Butterworth Highpass


#### Gaussian Highpass


#### Laplacian Filter


#### Unsharp Mask Filter


#### High Boost Filter


### Bandreject Filters


### Bandpass Filters
