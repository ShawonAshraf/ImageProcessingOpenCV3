from face_rec import detect_faces, show_result


images = ['images/im1.jpg', 'images/bm.jpg', 'images/rm.jpg']
image = images[0]

print("For image = {}".format(image))
im_tup = detect_faces(image)
show_result(im_tup)
