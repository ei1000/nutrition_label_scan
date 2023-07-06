import cv2 as cv
import os 
import numpy as np
from time import sleep

print(os.getcwd())



#Taking pictures with the camera
def captureImg(name):
        #The camera
        cam = cv.VideoCapture(0, cv.CAP_DSHOW)
        success, img = cam.read()

        cv.imwrite('imgs/test.png', img)


def pre_pros(img_path):
        img = cv.imread('imgs/yogurt/food_test.jpg')

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        #2d convolution
        #kernel2 = np.ones((5, 5), np.float32)/25
        #img = cv.filter2D(src=gray, ddepth=-1, kernel=kernel2)

        #Gaussian blur
        gaussian = cv.GaussianBlur(gray, (3,3), 0)

        #Contrasting with histogram equalization
        equ = cv.equalizeHist(gaussian)

        #Even out background with bilateral filter. - on the fence on this one, because the text loose a lot of visibility
        bilateral = cv.bilateralFilter(equ, 1, 5, 5)

        #Thresholding with gaussian to set very dark pixels to black and vice versa. Gaussian takes neighbours into consideration. Black and white img
        tresh = cv.adaptiveThreshold(bilateral, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 199, 30)

        
        #Finding the contours - THIS IS NOT OPTIMAL. THE REST OF PREPROCESSING MAKES THE PICTURES GOOD FOR EXTRACTING BUT AUTO FINDING WHAT 
        #SHOULD BE IN THE EXTRACTING PROCESS WITH CONTOURS IS A NIGHTMARE. INSTEAD USER INTERFACE WHERE THE USER CHOOSES THE 4 CORNERS OF THE LABEL.

        cv.imwrite('imgs/yogurt/yogurt_tresh.jpg', tresh)

def displayImg(img_path):
        img = cv.imread('imgs/test_pros.png')

        cv.imshow('ok', img)

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
        
#sharpening the img
        #kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        #sharpened = cv.filter2D(img, -1, kernel)

#sharpening the img
        #kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        #sharpened = cv.filter2D(img, -1, kernel)

#captureImg('test')
#detectBarcode('E:/Git/barcode_project/barcode_img.png')
pre_pros('imgs/food_test.jpg')
#displayImg('imgs/test')