import cv2
import numpy as np

from image_processing import ObjectClassifier

cap = cv2.VideoCapture(0)
oc = ObjectClassifier()

while True:

    ret, img = cap.read()

    classific = oc.classify(img)

    oc.annotate_class(img, classific)

    cv2.imshow('Classifier', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
