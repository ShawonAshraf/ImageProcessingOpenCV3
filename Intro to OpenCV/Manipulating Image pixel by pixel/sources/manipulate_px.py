import numpy as np
import cv2

image = cv2.imread('../images/kids_field_bangladesh.jpg', cv2.IMREAD_UNCHANGED)

threshold = np.amax(image)

for x in np.nditer(image, op_flags=['readwrite']):
    if x >= threshold / 2:
        x[...] = 1
    elif x < threshold / 2:
        x[...] = 0

print(image)

cv2.imshow('binary image', image)

key = cv2.waitKey(0)
if key == 27 or ord('q'):
    cv2.destroyAllWindows()
