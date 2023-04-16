#import cv2
import cv2
# lecture de l'image
man=cv2.imread('man.jpeg')
#niveau de gris
mangris=cv2.imread('man.jpeg',cv2.IMREAD_GRAYSCALE)
# lire face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(mangris, scaleFactor=1.1, minNeighbors=5)
#dessiner un rectangle autour de la face
for (x,y,w,h) in faces:
    #draw rectangles on faces
    cv2.rectangle(man,(x,y),(x+w,y+h),(255,0,0),2)
#afficher l'image
cv2.imshow('visage',man)
cv2.waitKey(0)
cv2.destroyAllWindows()