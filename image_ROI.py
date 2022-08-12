import numpy as np
import cv2

img = cv2.imread("image_dot.jpg")
img = cv2.resize(img,(1280,720))

roi=cv2.selectROI(img)
x, y, w, h = roi
print(x,y,w,h)


#roi_points = img[150:450, 400:900]
roi_points = img[y:y+h, x:x+w]
cv2.imshow("img",roi_points)
cv2.waitKey(0)
cv2.destroyAllWindows()