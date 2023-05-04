import cv2
import numpy as np

path = "/home/shreya/College/Computer Science/final year project/blur_glare_old/blur_glare/meeks_uncle_dl.jpg"
img = cv2.imread(path, 0)
width, height = 435, 277
image = cv2.resize(img, (width, height))
laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
blur_threshold = 400

# if laplacian_var< blur_threshold:
# print('Image is blurred.')
img_blur = cv2.GaussianBlur(image, (5, 5), 0)  # to reduce noise
laplacian = cv2.Laplacian(img_blur, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
sharpened = cv2.addWeighted(image, 1.4, laplacian, -0.8, 0)
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""else:
    print('Image is not blurred.')"""
