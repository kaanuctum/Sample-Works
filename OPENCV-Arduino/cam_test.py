#just to test if the camera is working
#doesn't do anything fancy

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
stand_size=(1080,720)#the size the frames will be,so its standardized
while True:
    #capture frame by frame
    ret,frame = cap.read()
    #resize it to standardize the results
    frame=cv2.resize(frame,stand_size)

    img_item = 'my-image.png'
    cv2.imwrite(img_item, frame)

    #Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ('q'): break
#when everything is done ,release the capture
cap.release()
cv2.destroyAllWindows()
