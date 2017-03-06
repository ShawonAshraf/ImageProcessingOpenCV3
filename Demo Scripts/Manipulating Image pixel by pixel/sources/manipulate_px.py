import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('../images/kids_field_bangladesh.jpg', cv2.IMREAD_GRAYSCALE)

thresh = 127
for x in np.nditer(image, op_flags=['readwrite']):
    if x >= thresh:
        x[...] = 1
    elif x < thresh:
        x[...] = 0


plt.imshow(image, cmap='gray')
plt.show()
