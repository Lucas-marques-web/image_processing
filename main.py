import cv2
import os


img = cv2.imread(os.path.join('.','image_processing/mario.png'))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb2 = cv2.cvtColor(img,cv2.COLOR_YCR_CB2BGR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rgb2',img_rgb2)

cv2.waitKey(0)