"""
Reads a image. Or in simpler terms, loads an image
and shows it in a window.
"""

import cv2

# image_file = '../images/bangladesh.jpg'
image_file = input('Enter path to image : ')

# loads the image
image = cv2.imread(image_file, cv2.IMREAD_UNCHANGED);

# view the image
cv2.imshow('OpenCV # 1, reading an image', image)

# code for the quit button to work

waitKey = cv2.waitKey(0)

# 27 = esc
# pressing esc or q will quit the window

if waitKey == 27 or waitKey == ord('q'):
    cv2.destroyAllWindows()
