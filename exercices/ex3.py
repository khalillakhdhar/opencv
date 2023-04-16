import cv2
import numpy as np

# Créer un objet de soustraction de fond
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Charger les deux images
image1 = cv2.imread("../image1.jpg")
image2 = cv2.imread("../image2.jpg")

# Appliquer la soustraction de fond aux images
foreground_mask1 = background_subtractor.apply(image1)
foreground_mask2 = background_subtractor.apply(image2)

# Appliquer un flou gaussien pour supprimer le bruit
blur_foreground_mask1 = cv2.GaussianBlur(foreground_mask1, (5, 5), 0)
blur_foreground_mask2 = cv2.GaussianBlur(foreground_mask2, (5, 5), 0)

# Calculer la différence entre les masques de premier plan
diff_mask = cv2.absdiff(blur_foreground_mask1, blur_foreground_mask2)

# Afficher l'image des différences
cv2.imshow("Image des differences", diff_mask)

# Attendre jusqu'à ce que l'utilisateur appuie sur une touche
cv2.waitKey(0)

# Fermer toutes les fenêtres
cv2.destroyAllWindows()
