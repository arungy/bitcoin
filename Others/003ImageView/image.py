import sys
import cv2
import numpy as np

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
def main():
    #load an image
    img = cv2.imread('Google_2015_logo.png', cv2.IMREAD_UNCHANGED )
    
    #display an image
    window_name = 'image'
    
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    sys.exit(1)
    