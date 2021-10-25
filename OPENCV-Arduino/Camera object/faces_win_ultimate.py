import numpy as np
import cv2





#allows you to set the brightness, contrast, size,
#and the number of cameras that will be used

standart_size = (1080,720)
brightness = 25. # brightness
contrast = 20.  # contrast




while True:
    cam_number = input('enter the amount of cameras that will be used(1 or 2): ')
    
    if cam_number =='1' or cam_number == '2' :
        cam_number = int(cam_number)
        break
    else: print('not a valid input')


face_cascade = cv2.CascadeClassifier(r'C:\Users\kaan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')

cap1 = cv2.VideoCapture(0)
if cam_number == 2 :cap2 = cv2.VideoCapture(1)
i=0


while True:
    #capture frame by frame
    ret1,frame1 = cap1.read()
    if cam_number == 2 : ret2,frame2 = cap2.read()
    
    #adjust the brightness and contrast
    frame1 = cv2.addWeighted(frame1, 1. + contrast/127., frame1, 0, brightness-contrast)

    
    cv2.resize(frame1,standart_size)
    if cam_number == 2: cv2.resize(frame2,standart_size)


    
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces1:
        i=0
        print(x,y,w,h)
        #roi = region of interest
        roi_gray  = gray1[y:y+h, x:x+w] #(y cord start, y cord end)
        roi_color = frame1[y:y+h, x:x+w]
        img_item = 'my-image.png'
        cv2.imwrite(img_item, roi_color)

        color = (255,0,0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame1, (x,y), (end_cord_x,end_cord_y), color, stroke)

    if cam_number == 2 :
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        faces2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.5, minNeighbors=5)
        for (x,y,w,h) in faces2:
            i=0
            print(x,y,w,h)
            #roi = region of interest
            roi_gray  = gray2[y:y+h, x:x+w] #(y cord start, y cord end)
            roi_color = frame2[y:y+h, x:x+w]
            img_item = 'my-image.png'
            cv2.imwrite(img_item, roi_color)
    
            color = (255,0,0) #BGR 0-255
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame2, (x,y), (end_cord_x,end_cord_y), color, stroke)



        
    #Display the resulting frame
    cv2.imshow('camera 1',frame1)
    if cv2.waitKey(20) & 0xFF == ('q'): break
    if cam_number == 2 :
        cv2.imshow('camera 2',frame2)
        if cv2.waitKey(20) & 0xFF == ('q'): break
#when everything is done ,release the capture
cap.relase()
cv2.destroyAllWindows()
