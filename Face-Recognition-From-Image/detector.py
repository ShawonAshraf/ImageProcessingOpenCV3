from face_rec import detect_faces, show_result


images = ['im1.jpg', 'bm.jpg', 'rm.jpg']
image = images[0]

print("For image = {}".format(image), end='')
im_tup = detect_faces(image)
show_result(im_tup)
