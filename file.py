import cv2

img=cv2.imshow("image.jpg")
print(img.shap)
#imgResize=cv2.resize(img,(1000,1200))
imgCropped=img[0:200,200:500]