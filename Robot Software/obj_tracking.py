import cv2 
import matplotlib.pyplot as plt 
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    bbox, label, conf = cv.detect_common_objects(frame)

    output_image  = draw_bbox(frame, bbox, label, conf)

    cv2.imshow('Result', output_image)


    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()