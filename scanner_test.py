import cv2 as cv
import os 
import numpy as np
from time import sleep

print(os.getcwd())
cam = cv.VideoCapture(0, cv.CAP_DSHOW)


def captureImg():
        success, img = cam.read()

        #flipping img
        #img = cv.flip(img, 1)

        #sharpening the img
        #kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        #sharpened = cv.filter2D(img, -1, kernel)

        #saving
        cv.imwrite('E:/Git/barcode_project/barcode_img.png', img)


def displayImg(img_path):
        img = cv.imread(img_path)

        cv.imshow('barcode_img.png', img)

        cv.waitKey(0) #If you want to wait for a specific key, use cv.waithek(0) == ord('key')
        cv.destroyAllWindows()


# while cam.isOpened():
#         status, frame = cam.read()
#         frame = cv.flip(frame,1)
#         detectBarcode(frame)
#         cv.imshow("ok", frame)
#         sleep(0.2)
#         if cv.waitKey(1) & 0xFF == ord('q'):
#                 break
        
                

#captureImg()
#detectBarcode('E:/Git/barcode_project/barcode_img.png')
#displayImg('E:/Git/barcode_project/barcode_img.png')