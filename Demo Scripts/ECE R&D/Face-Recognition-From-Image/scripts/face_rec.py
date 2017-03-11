import numpy
import cv2
from matplotlib import pyplot as plt


def detect_faces(impath):
    scale_factor = 1.1
    mask = 7
    min_size = (30, 30)

    scale_f = cv2.CASCADE_SCALE_IMAGE

    face_cascade = cv2.CascadeClassifier(
        '../classifiers/haarcascade_frontalface_default.xml')

    img = cv2.imread(impath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find faces as rectangles
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor,
                                          minNeighbors=mask,
                                          minSize=min_size,
                                          flags=scale_f)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite('../dump/out.jpg', img)

    return (img, faces)


def show_result(img_tup):
    cv2.imshow('Detected Faces', img_tup[0])
    k = cv2.waitKey(0)
    if k == 27 or k == ord('q'):
        cv2.destroyAllWindows()
