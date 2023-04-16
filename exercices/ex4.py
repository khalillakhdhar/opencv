import cv2

# Charger l'image
image = cv2.imread("car.jpg")

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un seuillage pour binariser l'image
ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

# Trouver les contours dans l'image binaire
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner les contours sur l'image d'origine
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Afficher l'image avec les contours dessinés
cv2.imshow("Image avec contours", image)

# Attendre jusqu'à ce que l'utilisateur appuie sur une touche
cv2.waitKey(0)

# Fermer toutes les fenêtres
cv2.destroyAllWindows()
