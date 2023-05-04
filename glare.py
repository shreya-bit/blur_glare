import cv2
import numpy as np

img = cv2.imread('sujay_dl.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

std_dev = np.std(gray)

if std_dev > 30:
    print('Glare is present in the image')
    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    result = cv2.medianBlur(opening, 5)
else:
    print('No glare is present in the image')


cv2.imshow('Original Image', img)
cv2.imshow('Processed Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
