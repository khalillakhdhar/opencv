import cv2
import numpy as np

# Charger les deux images
image1 = cv2.imread("../image1.jpg")
image2 = cv2.imread("../image2.jpg")

# Convertir les images en niveaux de gris
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien pour supprimer le bruit
blur_image1 = cv2.GaussianBlur(gray_image1, (5, 5), 0)
blur_image2 = cv2.GaussianBlur(gray_image2, (5, 5), 0)

# Calculer la différence MSE entre les deux images
diff_image = cv2.absdiff(blur_image1, blur_image2)
mse = np.mean(diff_image ** 2)

# Afficher l'image des différences MSE
cv2.imshow("Image des differences MSE", diff_image)
print("MSE différence MSE: {}".format(mse))
if mse<0.1:
    print("Les images sont identiques")
else:
    print("Les images sont différentes")
# Attendre jusqu'à ce que l'utilisateur appuie sur une touche
cv2.waitKey(0)

# Fermer toutes les fenêtres
cv2.destroyAllWindows()
