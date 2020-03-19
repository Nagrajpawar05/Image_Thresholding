import cv2
img = cv2.imread('image.png',0)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
#cv2.adaptiveThreshold(img,MAx_value,adaptive threshold_type,threshold_type,blockSize,constant)


th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2);


#Blocksize: it decides the neighbourhood area
#Constant : it is subtracted from the mean
#i.e (block_size x block_size) - C



cv2.imshow("image",img)
cv2.imshow('TH_image',th2)
cv2.imshow('TH1_image',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
