import cv2

# Capture de la vidéo en direct
cap = cv2.VideoCapture(0)

# Initialisation de la soustraction de fond
subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Lecture des images de la vidéo
    ret, frame = cap.read()

    # Soustraction de fond
    fgmask = subtractor.apply(frame)

    # Dilatation de l'image binaire pour remplir les trous
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    # Trouver les contours de l'image binaire
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner les contours sur la frame originale
    for c in contours:
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Afficher les frames
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)

    # Sortir en appuyant sur la touche ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Libération des ressources
cap.release()
cv2.destroyAllWindows()