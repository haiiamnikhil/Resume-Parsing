import cv2 as cv
import os as os

imagedir = "Files"

for image in os.listdir(imagedir):
    read_image = cv.imread(os.path.join("Files",image))
    resize = cv.resize(image,(50,100))
    predection = model.predict()
    print(predection)
