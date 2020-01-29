import cv2 as cv
import numpy as np
import pandas as pd
import os as os

imagepath = "images"

def crop_image(resize_image):




def dataframe(resize_image,coordinates):
    train_data = pd.DataFrame(resize_image).T
    train_label = pd.DataFrame(coordinates).T
    train_data.to_csv("traindata.csv",mode='a',index=None)
    train_label.to_csv("trainlabels.csv",mode="a",index=None)


for images in os.listdir(imagepath):
    read_image = cv.imread(os.path.join("images",images),1)
    if read_image is True:

        resize_image = cv.resize(read_image,(50,100))
        crop_image(resize_image)
        print(f"Image {count} -----[Sucess] Status!!!")
    
    else:
        print("Image is Not Readble [Failure]")