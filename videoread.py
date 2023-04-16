import cv2
#lecture de video video.mp4
cap=cv2.VideoCapture('video.mp4')
#cap=cv2.VideoCapture(0) pour la caméra
#cap=cv2.VideoCapture("https://www.pexels.com/video/video-of-woman-being-examined-8090200/") #pour la caméra ip ou url ouverte

# lecture en boucle
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        cv2.imshow('Vidéo',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
    