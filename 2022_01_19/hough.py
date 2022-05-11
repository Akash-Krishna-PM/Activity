import cv2
import numpy as np
img=cv2.imread("C:/Users/Windows 10/Downloads/sudoku.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,50)
cv2.imshow("Original",img)
#output vector of edges of lines
lines=cv2.HoughLines(edges,1,np.pi/180,200)
for line in lines:
    rho,theta=line[0]
    x0=rho*np.cos(theta)
    y0=rho*np.sin(theta)
    x1=int(x0-1000*np.sin(theta))
    y1=int(y0+1000*np.cos(theta))
    x2=int(x0+1000*np.sin(theta))
    y2=int(y0-1000*np.cos(theta))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)
    print(f"points:({x1},{y1}),({x2},{y2})")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()