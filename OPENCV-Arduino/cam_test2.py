#allows the smultanious usage of two cameras
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cascades/data/haarcascade_frontalface_alt2.xml')

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
i=0
while True:
    #capture frame by frame
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()

#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
#    for (x,y,w,h) in faces:
#        i=0
#        print(x,y,w,h)
#        #roi = region of interest
#        roi_gray  = gray[y:y+h, x:x+w] #(y cord start, y cord end)
#        roi_color = frame[y:y+h, x:x+w]
#        img_item = 'my-image.png'
#        cv2.imwrite(img_item, frame)

#        color = (255,0,0) #BGR 0-255
#        stroke = 2
#        end_cord_x = x + w
#        end_cord_y = y + h
#        cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color, stroke)
    #Display the resulting frame
    cv2.imshow('1',frame1)
    if cv2.waitKey(20) & 0xFF == ('q'): break
    cv2.imshow('2',frame2)
    if cv2.waitKey(20) & 0xFF == ('q'): break
#when everything is done ,release the capture
cap.relase()
cv2.destroyAllWindows()
