# Harshini Raju
# Human Detection using OpenCV

import cv2
import imutils

def humandetect(imagePath):
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())
    orig = image.copy()
    # detect people in the image
    (humans, weights) = hog.detectMultiScale(image,  
                                        winStride=(5,5), 
                                        padding=(25,25), 
                                        scale=1.05)
    for (x, y, w, h) in humans:
    	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # getting no. of human detected
    cv2.imshow("After NMS", image)
    cv2.waitKey(0)
    return len(humans)
    
imagePath='D:/Human Detection/Dataset/queue.jpg'
no_of_humans=humandetect(imagePath)
print(no_of_humans)