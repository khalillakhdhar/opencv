# import cv2
import cv2
#lecture de image simple (image1)
imcl=cv2.imread("image1.jpg",cv2.IMREAD_COLOR)
#lecture de image simple (image1) niveau de gris
imgris=cv2.imread("image1.jpg",cv2.IMREAD_GRAYSCALE)
#affichage de l'image
cv2.imshow("image couleur",imcl)

cv2.imshow("image gris",imgris)
cv2.waitKey(0)

