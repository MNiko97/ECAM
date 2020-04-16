# transformpict.py
# Author: Sébastien Combéfis
# Version: April 15, 2020

import imageio
import scipy as np

# Opening the tiger picture you can find here:
# https://www.flickr.com/photos/31004716@N00/3732644607
# The returned ndarray has three dimensions: the width, the height and
# the number of layers (3 for RGB picture, 4 for RGBA picture, etc.)
im = imageio.imread('tiger.jpg')

# Darkening the picture by dividing the RGB values of each pixel by 2
# and ensuring the value remains in [0; 255]
im = np.maximum(0, im / 2)

# Writing the new picture without forgetting to convert the values
# from float to uint8 (because of the operations previously performed)
imageio.imwrite('tiger-transformed.jpg', im.astype(np.uint8))