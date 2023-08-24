## importing packages
import os
import numpy as np
from PIL import Image
import cv2
import pathlib

## source dataset with grayscale board images
path = '/home/stark/thesis/sram/dataxmc/tflite/dataset/intact'

## destination to save RGB converted images
dest_path = '/home/stark/thesis/sram/dataxmc/tflite/dataset/intact-rgb'

## fetching grayscale images from the source folder
folders = []
for foldername in os.listdir(path):
    if foldername.startswith('board'):
        folders.append(foldername)

## creating target folders with same name as source folder
for folder in folders:
    os.mkdir(os.path.join(dest_path,folder))
    print(folder)
 

## file processing
for folder in folders:
    for file in os.listdir(os.path.join(path,folder)):
        if file.startswith('board'):

            ## in case of using pillow for conversion
            #image = Image.open(os.path.join(path,folder,file)).convert("RGB")
      
            ## inase of using opencv
            image = cv2.imread(os.path.join(path,folder,file), cv2.IMREAD_GRAYSCALE)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

            # re-write file after conversion
            new_filename = os.path.splitext(file)[0] + '_rgb.png'
            print(new_filename)
      
            ## pillow
            #image.save(os.path.join(dest_path,folder,new_filename))

            ## opencv
            cv2.imwrite(os.path.join(dest_path,folder,new_filename), image_rgb)
