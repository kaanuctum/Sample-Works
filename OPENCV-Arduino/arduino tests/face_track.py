import numpy as np
import cv2
import pyfirmata
import time

# don't forget to change the serial port to suit
board = pyfirmata.Arduino('COM7')
#ports of the connected servos(should be updated accordingly)
pin_x = board.get_pin('d:9:s')
pin_y = board.get_pin('d:13:s')

width  = 1980
height = 1080

x_state = 90
y_state = 90

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
pin_x.write(x_state)
pin_y.write(y_state)



face_cascade = cv2.CascadeClassifier('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
i=0
while True:
    #capture frame by frame
    ret,frame = cap.read()
    frame = cv2.resize(frame,(width,height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    fn = 0
    for (x,y,w,h) in faces:
        fn+=1
        if fn != 1 : continue
        print(x,y,w,h)
        #roi = region of interest
        roi_gray  = gray[y:y+h, x:x+w] #(y cord start, y cord end)
        roi_color = frame[y:y+h, x:x+w]
        #img_item = 'my-image.png'
        #cv2.imwrite(img_item, roi_color)

        x_pixel = x+(w/2)
        y_pixel = y+(h/2)

        x_dist  = (width/2)   - x_pixel
        y_dist  = (height/2)  - y_pixel
        

        x_angle = x_dist/500
        y_angle = y_dist/-500




        rotated = False
        if x_dist< 50 or x_dist >-50:
            if (x_state + x_angle)<260 and (x_state + x_angle)>0 :x_state += x_angle
            pin_x.write(x_state)
        if y_dist< 50 or y_dist >-50:
            if (y_state + y_angle)<260 and (y_state + y_angle)>0 :y_state += y_angle
            pin_y.write(y_state)







        color = (255,0,0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color, stroke)
    #Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ('q'): break
#when everything is done ,release the capture
cap.relase()
cv2.destroyAllWindows()
