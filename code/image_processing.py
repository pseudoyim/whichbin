'''
The image processing module for WhichBin. Classifies the object in hand and detects the appropriate bin to put it in.
Written for cv2 v3.1.0
'''

from keras.preprocessing import image as image_utils
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from bin_contents import dict_bins

import cv2
import json
import numpy as np


class ObjectClassifier(object):

    def __init__(self):
        self.model = VGG16(weights='imagenet', include_top=True)
        imagenet_json = '../data/imagenet_class_index.json'
        self.CLASS_INDEX = json.load(open(imagenet_json))

    def classify(self, img):

        # Find the height (number of rows).
        height, width = img.shape[0], img.shape[1]
        margin = height/2.
        mid = width/2.

        # Make the width the same as the height, but keep the same center (mid) as before.
        img_middle = img[ : , mid - margin : mid + margin]

        # Then resize.
        img_small = cv2.resize(img_middle, (224, 224))

        x = image.img_to_array(img_small)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        pred_array = self.model.predict(x)
        argmax_index = np.argmax(pred_array)
        classification = self.CLASS_INDEX[str(argmax_index)][1]
        correct_bin = ''

        for k,v in dict_bins.iteritems():
            if classification in v:
                correct_bin = k

        return correct_bin

    def annotate_class(self, img, correct_bin):

        cv2.putText(img, "THROW THIS INTO: {}".format(correct_bin), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), thickness=2)
