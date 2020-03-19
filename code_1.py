import cv2
from matplotlib import pyplot as plt
img = cv2.imread('image.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th_1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)  #cv2.threshold(img,threshold_value,max_value,Threshold_type)
                                                    
ret,th_2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #inverse result of th_1

ret,th_3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC) 

ret,th_4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

ret,th_5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) 

titles=['Original','Binary','Binary_inv','Trunc','Tozero','Tozero_inv']
images=[img,th_1,th_2,th_3,th_4,th_5]

for i in range(0,6):
    plt.subplot(2,3,i+1) #plt.subplot(rows,colums,index)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

#cv2.imshow('image',img)
#cv2.imshow('thre',th_5)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
