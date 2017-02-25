"""
Reads a image. Or in simpler terms, loads an image
and shows it in a window.
"""

import cv2


# loads the image as it is
image = cv2.imread('../images/bangladesh.jpg', cv2.IMREAD_UNCHANGED);

# display the image
cv2.imshow('OpenCV - reading an image', image)

# handling a bit of gui
waitKey = cv2.waitKey(0)

# pressing escape quits the program
# pressing s will save the loaded image in the
# output_images directory

if waitKey == 27:
    cv2.destroyAllWindows()
elif waitKey == ord('s'):
    cv2.imwrite('../output_images/unaltered.jpg', image)
    cv2.destroyAllWindows()
