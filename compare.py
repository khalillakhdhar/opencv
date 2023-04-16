import cv2
image1=cv2.imread("image1.jpg")
image2=cv2.imread("image1.jpg")
# calculer mse entre les images
mse = ((image1 - image2) ** 2).mean()

imgout=image1-image2
cv2.imshow("image de différence",imgout)
cv2.waitKey(0)
# afficher la différence entre les images
print("MSE: {}".format(mse))
#ssim = cv2.compare_ssim(image1, image2, multichannel=True)
#print('SSIM:', ssim)
if(mse<0.1):
    print("les images sont identiques")
else:
    print("les images ne sont pas identiques")