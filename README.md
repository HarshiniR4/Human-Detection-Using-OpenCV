# Human-Detection-Using-OpenCV

The purpose of this project is to build a Human detection model using OpenCV. For that purpose we are going to first detect humans in the image, then create a function that returns the count of humnas in the picture


## Dataset 
[Human Detection Dataset from Kaggle](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset)

**Assumptions**: As the model utilises the HOG model of OpenCV the data to be used must only be restricted to full-body clear colour images of humans in the location.

## Modules
- cv2
- imutills

## Steps
- Import necessary modules
- Read image needed using the cv2 module
- Load the pre-trained HOG and Linear SVM Model
- Load the People Detector function in the HOG model of OpenCV
- Resize the image according to the requirements- taken 500 as standard
- With the detectMultiScale() function identify the boxes i.e., humans in the picture and their weights
-Apply the contours for the humans detected and display the final output
- Developed a function that takes in the image path and returns the number of humans identified in the picture with the image displayed.

## Output

![image](https://user-images.githubusercontent.com/59364581/179677340-fce6ca93-d2ac-4610-a11a-4b495ecc2464.png)

![image](https://user-images.githubusercontent.com/59364581/179677376-58e71638-a413-4f18-a9d1-d7cdc6d7537d.png)


**Harshini Raju**
