import cv2
import numpy as np

img = cv2.imread("anya.jpg")
img = cv2.resize(img, (640, 480))
mask = np.zeros(img.shape, np.uint8)

points  = np.array([[273,167], [363, 167], [573, 353], [63, 353]])  ##taking random points for ROI.
cv2.fillPoly(mask, [points], (100, 0, 100))

img = cv2.addWeighted(img, 0.7, mask, 0.5, 0)

values = img[np.where((mask == (100, 0, 100)).all(axis=1))]
print(values)

val = np.where(mask < 0)
coordinate = list(zip(val[0], val[1]))
print(coordinate)

##cv2.imshow("mask", mask)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()