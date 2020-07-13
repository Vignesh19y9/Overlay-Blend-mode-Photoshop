import numpy as np
import cv2

a = cv2.imread("input.jpg", cv2.IMREAD_UNCHANGED)
b = cv2.imread("input.jpg", cv2.IMREAD_UNCHANGED)

a = a.astype(float)/255
b = b.astype(float)/255


mask = a >= 0.5 # generate boolean mask of everywhere a > 0.5 
ab = np.zeros_like(a) # generate an output container for the blended image 

# now do the blending 
ab[~mask] = (2*a*b)[~mask] # 2ab everywhere a<0.5
ab[mask] = (1-2*(1-a)*(1-b))[mask] # else this 

x=(ab*255).astype(np.uint8) 

cv2.imshow("water", x)
cv2.waitKey(0)
