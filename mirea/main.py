from PIL import Image
import cv2

capture = cv2.VideoCapture(0)
capture2 = cv2.VideoCapture(r"C:\Users\Propolisss\Downloads\Telegram Desktop\2021-11-22 20-35-12.mp4")

capture2.set(3,1280)
capture2.set(4,700)

face_cascade = cv2.CascadeClassifier(r"C:\Users\Propolisss\opencv\data\haarcascades\haarcascade_frontalface_default.xml")



while True:
    ret, img = capture2.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('rez camera', img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture2.release()
cv2.destroyAllWindows()