import cv2
import time
import numpy as np
import os
os.chdir('C:/Users/Adam/Downloads/6IICT_PROG4_oef/motion detection/vormen.png')

img = cv2.imread('vormen.png')
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image
cropped_image = img[80:280, 150:330]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.png", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
