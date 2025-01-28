
import cv2
import numpy

#initializing the default camera with parameter 0
cap = cv2.VideoCapture(0)

#face Detection 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

skip=0

while True :
    ret, frame = cap.read()

    if ret== False:
        continue


    faces = face_cascade.detectMultiScale(frame,1.3,5)
    print (faces)

    for face in faces :
        (x,y,w,h)= face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow("Frame",frame)


#storing every 10th face
    if (skip%10==0):
        #store 10th face later on
        pass

   
    key_pressed= cv2.waitKey(0) & 0xFF
    if key_pressed == ord("q"):
        break

cap.release()
cap.destroyAllWindows()











