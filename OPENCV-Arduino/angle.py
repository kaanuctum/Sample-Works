from pyfirmata import Arduino, util
import time
import numpy as np
import distance

def angle(width,x_pixel,max_alpha):
    i = (width/2)/np.tan(np.deg2rad(max_alpha))
    pixel_dist = (width/2)-x_pixel
    if pixel_dist < 0: pixel_dist = pixel_dist*-1
    alpha = np.rad2deg(np.arctan(pixel_dist/i))
    if x_pixel < width/2:
        return -1*alpha
    if x_pixel >= width/2:
        return alpha


#these values should allready be given
    #size of the cam screen
height
width

    #location of the up left corner of the face square and
x,y
#the size of the face square
w,h

#ports of the connected servos(should be updated accordingly)
servo_x = 13
servo_y = 9
servo_speed=0.2 #the time it takes the servo to rotate 1 degree in seconds

#connect the arduino board
board = Arduino('com3')

x_pixel = x+(w/2)
y_pixel = y+(h/2)

while True:

    x_angle= angle(width,  x_pixel, max_alpha)
    y_angle= angle(height, y_pixel, max_alpha)
    
    x_dist = x_pixel - width/2
    y_dist = y_pixel - height/2
    
    rotated = False
    if x_dist< 10 or x_dist >-10:
        board.digital[servo_x].write(x_angle)
        rotated = True
    if y_dist< 10 or y_dist >-10:
        board.digital[servo_y].write(y_angle)
        rotated = True
    if rotated is True:
        if x_angle < y_angle: time.sleep(servo_speed*y_angle)
        else:time.sleep(servo_speed*x_angle)











    
 
