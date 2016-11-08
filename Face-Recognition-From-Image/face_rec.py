import numpy
import cv2


def detect_faces(impath):
    scale_factor = 1.1
    mask = 7
    min_size = (30, 30)

    scale_f = cv2.CASCADE_SCALE_IMAGE

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(impath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find faces as rectangles
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor,
                                          minNeighbors=mask,
                                          minSize=min_size,
                                          flags=scale_f)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite("out.jpg", img)

    return (img, faces)


def show_result(img_tup):
    print("Faces in image = {}".format(len(img_tup[1])))
    cv2.imshow('img', img_tup[0])
    # Window lasts for 30 seconds
    cv2.waitKey(1000 * 30)
    cv2.destroyAllWindows()
