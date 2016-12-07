'''
Identifies text in images.
1. Takes an input image, filters for edge detection.
2. Pass through pyTesseract for character recognition and prints what it finds.

PROBLEM:
Keep getting this error: AttributeError: 'numpy.ndarray' object has no attribute 'split'
Might have something to do with the text in the image being at an angle.
Does pytesseract only work on clean text images where the text is perfectly 'flat'?

'''

import cv2
import glob
import numpy as np
import sys
import time

from PIL import Image
from pytesseract import image_to_string

SIGMA = 0.33


def auto_canny(blurred):

    # Compute the median of the single channel pixel intensities
    global SIGMA
    v = np.median(blurred)

    # Apply automatic Canny edge detection using the computed median of the image
    lower = int(max(0,   (1.0 - SIGMA) * v))
    upper = int(min(255, (1.0 + SIGMA) * v))
    edged = cv2.Canny(blurred, lower, upper)
    return edged


def invert(image_orig):
    # Inverts images from black to white, vice versa.
    inverted = (255 - image_orig)
    return inverted

def read_text(input_img):

    gray    = cv2.imread(input_img, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    auto = auto_canny(blurred)
    auto_inverted = invert(auto)

    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filtered_img = 'img_tess_{}.jpg'.format(timestamp)

    cv2.imwrite(filtered_img, auto_inverted)

    # print image_to_string(Image.open(filtered_img))
    print image_to_string(auto)


if __name__ == '__main__':

    # Test images should be saved as jpgs in the 'images' folder.
    images = glob.glob('../images/*.jpg')

    for each in images:
        read_text(each)
