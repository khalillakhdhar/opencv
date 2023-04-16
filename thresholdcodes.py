import cv2
# Charger les deux images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')
# Convertir les images en niveaux de gris
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Calculer la différence absolue
diff = cv2.absdiff(gray1, gray2)
print(diff)
# Afficher l'image de différence
cv2.imshow('Différence absolue', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Calculer le seuil de différence
