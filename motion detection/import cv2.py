# import the opencv module
import cv2
import time
import numpy as np


img = cv2.imread('wolfhusky.jpg')
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image
cropped_image = img[80:280, 150:330]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

# capturing video
capture = cv2.VideoCapture(1)  

while capture.isOpened():
    # to read frame by frame
    _, img_1 = capture.read()
    _, img_2 = capture.read()

    # find difference between two frames
    diff = cv2.absdiff(img_1, img_2)

    # to convert the frame to grayscale
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # apply some blur to smoothen the frame
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)

    # to get the binary image
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    # to find contours
    contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # to draw the bounding box when the motion is detected
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print("beweging")
    # cv2.drawContours(img_1, contours, -1, (0, 255, 0), 2)

    # display the output
    cv2.imshow("Detecting Motion...", img_1)
    if cv2.waitKey(100) == 13:
        exit()