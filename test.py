import cv2
import numpy as np



cap = cv2.VideoCapture('walking_vid3.mp4')
ret, frame = cap.read()
#frame = cv2.resize(frame,(640,480))
roi=cv2.selectROI(frame)
x, y, w, h = roi
print(x,y,w,h)
#hs,ws, cs = cap.shape
#print(hs,ws,cs)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(1280,720))
    cv2.imwrite("image.jpg",frame)
    #roi_points=frame[y:h,x:w]
    roi_points = frame[y:y+h, x:x+w]
    #roi_points = frame[150:450, 400:900]
    #cv2.imshow("FRAME",frame)
    cv2.imshow("FRAME ROI",roi_points)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()

#roi = cv2.selectROI(frame)

#x, y, w, h = cv2.selectROI(vid)

#print(x,y,w,h)

