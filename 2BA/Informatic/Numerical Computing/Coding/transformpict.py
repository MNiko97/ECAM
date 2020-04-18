# transformpict.py
# Author: Sébastien Combéfis
# Version: April 15, 2020

import imageio, os
import numpy as np
import copy

# Opening the tiger picture you can find here:
# https://www.flickr.com/photos/31004716@N00/3732644607
# The returned ndarray has three dimensions: the width, the height and
# the number of layers (3 for RGB picture, 4 for RGBA picture, etc.)
ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/Numerical Computing/Coding/"
image = 'tiger.jpg'

# Darkening the picture by dividing the RGB values of each pixel by n
# and ensuring the value remains in [0; 255]
# Writing the new picture without forgetting to convert the values
# from float to uint8 (because of the operations previously performed)
def dark(image, n):
    im = imageio.imread(ROOT + image)
    im = np.maximum(0, image/n)
    imageio.imwrite(ROOT + 'tiger-transformed.jpg', im.astype(np.uint8))
    return im

def invertcolor(image):
    im = imageio.imread(ROOT + image)
    inverted = [255, 255, 255] - im[:][:]
    imageio.imwrite(ROOT + 'tiger-transformed.jpg', inverted.astype(np.uint8))
    return inverted

def crop(image, point1, point2):
    im = imageio.imread(ROOT + image)
    x1, y1 = point1
    x2, y2 = point2
    cropped = im[x1:x2, y1:y2]
    imageio.imwrite(ROOT + 'tiger-transformed.jpg', cropped.astype(np.uint8))
    return cropped
    
#print(crop(image, (0, 0), (500, 500)).shape)
#print(invertcolor(image).shape)