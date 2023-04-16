import cv2

# Charger l'image
image = cv2.imread("car.jpg")

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien pour supprimer le bruit
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Afficher l'image d'origine et l'image en niveaux de gris
cv2.imshow("Image originale", image)
cv2.imshow("Image en niveaux de gris", blur_image)

# Attendre jusqu'à ce que l'utilisateur appuie sur une touche
cv2.waitKey(0)

# Fermer toutes les fenêtres
cv2.destroyAllWindows()
# documentation
#Ce programme charge une image en couleur à partir d'un fichier et utilise la fonction cvtColor pour convertir l'image en niveaux de gris. Ensuite, il applique un flou gaussien en utilisant la fonction GaussianBlur pour supprimer le bruit de l'image en niveaux de gris. Enfin, il affiche l'image d'origine et l'image en niveaux de gris dans deux fenêtres séparées à l'aide de la fonction imshow. L'utilisateur doit appuyer sur une touche pour fermer les fenêtres en utilisant la fonction waitKey.