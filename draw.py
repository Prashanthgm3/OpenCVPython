import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype='uninta')
img = cv.imread('Photos/cat.img')
cv.imshow('Cat', img)

cv.waitKey(0)