import cv2

# Créer un objet de capture vidéo
capture = cv2.VideoCapture('video.mp4')

# Créer un objet de détection de visage
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Boucle pour traiter chaque image de la vidéo
while True:
    # Lire une image de la vidéo
    ret, frame = capture.read()

    # Arrêter la boucle si la vidéo est terminée
    if not ret:
        break

    # Convertir l'image en niveaux de gris
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détecter les visages dans l'image en niveaux de gris
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Afficher l'image avec les rectangles dessinés
    cv2.imshow("Video avec detection de visages", frame)

    # Attendre jusqu'à ce que l'utilisateur appuie sur une touche
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
capture.release()
cv2.destroyAllWindows()
