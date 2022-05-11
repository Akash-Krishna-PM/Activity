#Take smarties.png image file and perform all morphological operations and display it using matplotlib
#Clue: Colored Image so need to read in grayscale and mask it to binary as morphological operations are performed only on binary images.

import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("C:/Users/Windows 10/Downloads/smarties.jpeg",0)

#masking
mask=np.zeros(img.shape[:2],dtype="uint8")
mimg=cv2.bitwise_and(img,img,mask=mask)
kernel=np.ones((5,5),np.uint8)
erodeimg=cv2.erode(mimg,kernel,iterations=1)
dilatedImg=cv2.dilate(mimg,kernel,iterations=1)
morphOp=cv2.morphologyEx(mimg,cv2.MORPH_OPEN,kernel)
morphcl=cv2.morphologyEx(mimg,cv2.MORPH_CLOSE,kernel)
morphGra=cv2.morphologyEx(mimg,cv2.MORPH_GRADIENT,kernel)
morphth=cv2.morphologyEx(mimg,cv2.MORPH_TOPHAT,kernel)
morphbh=cv2.morphologyEx(mimg,cv2.MORPH_BLACKHAT,kernel)
titles=['Original','Erosion','Dilate','Opening','Closing','Gradient','Tophat','Blackhat']
images=[mimg,erodeimg,dilatedImg,morphOp,morphcl,morphGra,morphth,morphbh]
for i in range(len(titles)):
    plt.subplot(3, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], "gray")
    plt.xticks([])
    plt.yticks([])
plt.show()
