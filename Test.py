import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
img = cv2.imread('2002.bmp',0)
ret,thresh = cv2.threshold(img,226,255,0)

image,contours,hierarchy=cv2.findContours(thresh,1,2)
#imag = cv2.drawContours(image,contours,3,(0,255,0),3)
cnt=contours[0]
M=cv2.moments(cnt)
print(M)
print (len(contours))
#ret, thresh = cv2.threshold(img,226,255,cv2.THRESH_BINARY)
#binaryImg = cv2.Canny(img,230,255)

#image,contours,hierarchy=cv2.findContours(thresh,1,2)
##h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
##contours = h[0]
##print(type(h))
##print (len(contours))

##cnt=contours[0]
##print (cnt)
##M=cv2.moments(cnt)
##print(M)
###cv2.namedWindow("image")
plt.imshow(image,'gray')
plt.show()
#cv2.imshow("image",img)
#cv2.waitKey(0)        
#cv2.destroyAllWindows()   

##import matplotlib.pyplot as plt 
##import matplotlib.image as mpimg 
##import numpy as np
##
##lena = mpimg.imread('2002.bmp') 
##
##lena.shape #(512, 512, 3)
##
##plt.imshow(lena) 
##plt.axis('off') 
##plt.show()
