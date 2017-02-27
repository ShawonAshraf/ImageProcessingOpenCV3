import numpy as np
import cv2

from matplotlib import pyplot

image = cv2.imread('../images/kids_field_bangladesh.jpg', cv2.IMREAD_GRAYSCALE)

thresh = 127
for x in np.nditer(image, op_flags=['readwrite']):
    if x >= thresh:
        x[...] = 1
    elif x < thresh:
        x[...] = 0

cv2.imshow('preview', image)

k = cv2.waitKey(0)
if k == 27 or ord('q'):
    cv2.imwrite('../images/out.jpg', image)
    cv2.destroyAllWindows()
