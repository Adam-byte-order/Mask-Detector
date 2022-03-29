from os import P_DETACH
import pandas as pd
import cv2

#frame = cv2.imread("allImagesNoMask/train/1803151818-00000003.jpg")
def retallaCara(frame, threshold = 0):
    face_cascade = cv2.CascadeClassifier(
        'C:/Users/ger-m/anaconda3/pkgs/libopencv-4.0.1-hbb9e17c_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    crop_img = -1
    for (x, y, w, h) in faces:
        y = y - threshold
        x = x - threshold
        w = w + threshold
        h = h + threshold
        crop_img = frame[y:y+h, x:x+w]

    return crop_img

    