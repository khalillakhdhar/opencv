#import opencv cv2
import cv2
# lecture de votre webcam (0) 
cap=cv2.VideoCapture(0) #capture the video
#lecture en boucle
while True:
    ret,frame=cap.read() #lire la capture de vidéo en continue
    cv2.imshow('Vidéo',frame) #afficher la vidéo
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
