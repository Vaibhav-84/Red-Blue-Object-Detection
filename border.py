import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

# address = "http://192.168.31.112:8080/video"
# cap.open(address)
cap.set(3,640)
cap.set(4,480)

while True:
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower_red = np.array([0,80,120])
    # upper_red = np.array([10,255,255])

    lower_blue = np.array([90,60,0])
    upper_blue = np.array([121,255,255])

    mask1 = cv2.inRange(hsv,lower_blue,upper_blue)
    # mask2 = cv2.inRange(hsv,lower_red,upper_red)

    cnts1 = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    # cnts2 = cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cnts2 = imutils.grab_contours(cnts2)

    for c in cnts1:
        areal = cv2.contourArea(c)
        if areal > 5000:

            cv2.drawContours(frame,[c],-1,(0,255,0),3)
            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame,"Blue",(cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)
    # for c in cnts2:
    #     area2 = cv2.contourArea(c)
    #     if area2 > 5000:

    #         cv2.drawContours(frame,[c],-1,(0,255,0),3)
    #         M = cv2.moments(c)

    #         cx = int(M["m10"]/M["m00"])
    #         cy = int(M["m01"]/M["m00"])

    #         cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
    #         cv2.putText(frame,"Red",(cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)


    k = cv2.imshow("result",frame)

 
    key=cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()