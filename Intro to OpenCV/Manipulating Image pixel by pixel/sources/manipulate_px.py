import numpy as np
import cv2

image = cv2.imread('../images/kids_field_bangladesh.jpg', cv2.IMREAD_GRAYSCALE)

thresh = 127
for x in np.nditer(image, op_flags=['readwrite']):
    if x >= thresh:
        x[...] = 1
    elif x < thresh:
        x[...] = 0

cv2.imshow('binary image', image)

key = cv2.waitKey(0)
if key == 27 or ord('q'):
    cv2.imwrite('../images/out.jpg', image)
    cv2.destroyAllWindows()
