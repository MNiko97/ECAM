# transformpict.py
# Author: Mitrovic Nikola
# Version: April 19, 2020

import imageio, os
import numpy as np

# Opening the tiger picture you can find here:
# https://www.flickr.com/photos/31004716@N00/3732644607
# The returned ndarray has three dimensions: the width, the height and
# the number of layers (3 for RGB picture, 4 for RGBA picture, etc.)
ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"
image = 'tiger.jpg'
im = imageio.imread(ROOT + image)

# Darkening the picture by dividing the RGB values of each pixel by n %
# and ensuring the value remains in [0; 255]
def dark(image, n):
    factor = 100/n
    return np.maximum(0, image/factor)
    
# To invert color in a picture :
# Substract maximum value (255) to current value
# For each R, G, B level value of each pixels composing the image
def invertcolor(image):
    return [255, 255, 255] - image[:][:]

# Crop image given two points coordinate that form borders
# By only saving pixels between these borders
def crop(image, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return image[y1:y2, x1:x2]

# Testing all image processing methods : 
# Inverting color, cropping image and
# Darkening to 50% of the original value
inverted_image = invertcolor(im) 
cropped_image = crop(im, (325, 65), (1120, 905))
final_image = dark(im, 1)
imageio.imwrite(ROOT + 'transformed1.jpg', inverted_image.astype(np.uint8))
imageio.imwrite(ROOT + 'transformed2.jpg', cropped_image.astype(np.uint8))
imageio.imwrite(ROOT + 'transformed3.jpg', final_image.astype(np.uint8))