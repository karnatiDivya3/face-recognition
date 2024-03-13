import cv2

import sys

import os

import time

cam = cv2.VideoCapture(0)

cam.set(3, 640) # set video width

cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml")

#For each person, enter one numeric face id

face_id = input('\n enter user id end press angle return>=>^ + )

print("\n [INFO] Initializing face capture. Look the camera and wait

# Initialize individual sampling face count

count = 0

while(True):

ret, img cam.read()

#img = cv2.flip(img, 1) #flip video image vertically gray cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) faces face_detector.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:

cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

count += 1

#Save the captured image into the datasets folder cv2.imwrite("dataset/User." str(face_id) + '.' + str(count)".jpg", gray[y:y+h,x:x+w])

cv2.imshow('image', img)

if cv2.waitKey(100) & 0xff == ord('q'):

break

elif count >= 10: Take Be face sample and stop video

break

print("\n [INFO] Exiting Program and cleanup stuff")

cam, release()

cv2.destroyAllWindows()