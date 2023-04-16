#import cv2
import cv2
# lecture de l'image
car=cv2.imread('car.jpeg')
#niveau de gris
carg=cv2.imread('car.jpeg',cv2.IMREAD_GRAYSCALE)
# lire car cascade
car_cascade = cv2.CascadeClassifier('cars.xml')
cars = car_cascade.detectMultiScale(carg, scaleFactor=1.1, minNeighbors=5)
#dessiner un rectangle autour de la car
for (x,y,w,h) in cars:
    #draw rectangles on cars
    cv2.rectangle(car,(x,y),(x+w,y+h),(0,0,255),2)

# Détection des contours avec l'algorithme de Canny
edges = cv2.Canny(carg, 100, 200)
#afficher l'image
#cv2.imshow('cars',car)
cv2.imshow('Contours', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()