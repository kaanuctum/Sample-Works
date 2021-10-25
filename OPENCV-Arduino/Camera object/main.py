from Camera import Camera
import cv2
import numpy as np

cam = Camera()
#face_cascade = cv2.CascadeClassifier(r'C:\Users\kaan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')

while True:
    frame = cam.get_frame()
    eyes = cam.find_object(frame, 'eye')
    face = cam.find_object(frame, 'frontalface_alt')
    frame = cam.canny(frame)
    frame = cam.boxes(frame, face, color = (255,0,255))
    frame = cam.boxes(frame, eyes)
    cam.show(frame)
    if cv2.waitKey(25) & 0xFF == ('q'): break

cam.exit()
exit()
    
