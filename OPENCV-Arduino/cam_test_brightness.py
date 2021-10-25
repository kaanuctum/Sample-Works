#allows you to adjust brightness and contrast
import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

brightness = 0. # brightness
contrast = 0.  # contrast
while True:
    #capture frame by frame
    ret,frame = cap.read()

    #adjust the brightness and contrast
    frame = cv2.addWeighted(frame, 1. + contrast/127., frame, 0, brightness-contrast)

    #Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ('q'): break
#when everything is done ,release the capture
cap.relase()
cv2.destroyAllWindows()
