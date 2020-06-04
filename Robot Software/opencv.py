import numpy as np
import cv2 as cv

#img = cv.imread('images.png', 0)
#print(img)
#cv.imshow('image', img)
#cv.waitKey(0)
#cv.destroyAllWindows()

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret,frame = cap.read()
if not ret:
    exit() 

grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

cv.namedWindow('image')

def draw_circle(event, x, y, flags, param):
    print(event)
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("EV")
        cv.circle(grey, (x,y), 100, (255,0,0), -1)
    else:
        print("INC")

cv.setMouseCallback('image', draw_circle)

while True:
    cv.imshow('frame', grey)
    if cv.waitKey(20) & 0xFF == 27:
        break


cap.release()
cv.destroyAllWindows()