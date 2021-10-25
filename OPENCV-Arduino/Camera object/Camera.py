import numpy as np
import cv2

standart_size = (1080,720)

class Camera(object):
    def __init__(self, camera_number = 0):
        self.brightness = 0
        self.contrast = 0
        self.cap = cv2.VideoCapture(camera_number)
        self.size = (1080, 720)
        
    def canny(self, frame, th1=150, th2=300):
        #adjust the thresholds to adjust the sensitivity
        frame = cv2.Canny(frame, threshold1=th1, threshold2=th2)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        return frame
        
        


    def get_cascade(self, name):
        name = str(name)
        name = "cascades\haarcascade_" + name + ".xml"
        cascade = cv2.CascadeClassifier(name)
        return cascade
        

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_contrast(self, contrast):
        self.contrast = contrast

    def set_size (self, size):
        self.size = size

    def get_frame(self):
        _, frame = self.cap.read()
        #adjust the brightness and contrast
        frame = cv2.addWeighted(frame, (1. + self.contrast/127.) , frame, 0, (self.brightness-self.contrast))
        return frame
        
    def find_object(self, frame, cascade):
        cascade = self.get_cascade(cascade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objects = cascade.detectMultiScale(
            gray,
            scaleFactor = 1.5,
            minNeighbors = 5
            )
        return objects

    def boxes(self, frame, objects, color = (255,0,0), stroke = 2):#BGR 0-255
        for (x,y,w,h) in objects:
            end_cord_x = x+w
            end_cord_y = y+h
            cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color, stroke)
        return frame

    def show(self, frame, title = "camera"):
        cv2.imshow(title, frame)

        
            
    def exit(self):
        self.cap.relase()
        cv2.destroyAllWindows()
            
        
