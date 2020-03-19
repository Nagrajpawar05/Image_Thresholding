# Image_Thresholding

There are varios types of Thresholding operations available in OpenCv library. I have explained few of them which we often use:
1.Binary Thresholding:
         In this type the pixel value < threshold value will get assigned to 0 and the pixel value > threshold value will get 
         assigned to 1,so the will result a binary image(image with either 0(black) or 1(white) color pixel)
 
2.Binary_inverse Thresholding:
         Inverse of the first type!.
         
3.Trunc Thresholding:
         In this type the pixel value < Threshold value remain unaltered but the pixel value > threshold, will get assigned 
         threshold value
     
4.To_Zero Thresholding:
         In this type pixel_value < Threshold will get assigned to zero, pixel_value > Threshold value remain unaltered.
         
         
  ![Figure_1](https://user-images.githubusercontent.com/61599110/77090086-b110e080-6a2c-11ea-9e2f-5c4f060711b0.png)  
         
         
 All the above mentioned types corresponds to global thresholding where we should provide the threshold value and this value 
 is compared with all the pixels in the image.
 Well this type of operations will not meet our needs when the light conditions in image vary from pixel to pixel.
 Inorder to overcome this we have #Adaptive_Thresholding .
 
   Adaptive thresholding is a method to set the threshold value for a smaller region of image.
 
# Algorithms to perform Adaptive Thresholding:

1.Mean Adaptive Thresholding : Here the threshold value is the mean of neighbourhood values.
2.Gaussian Adaptive Thresholding : Here threshold value is the weighted sum of neighbourhood values where weights are gaussian
                                   window.

