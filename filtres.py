import cv2
img = cv2.imread('images.jpeg')
blur = cv2.GaussianBlur(img, (7, 7), 0)
#filtre2=cv2.medianBlur(img,5)
cv2.imshow('Blur Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()