## based on @reshmi's work https://github.com/reshmisuragani/Master-Thesis-ML-SRAM_PUF 
import os,glob
import random
from itertools import cycle,islice
from PIL import Image
import numpy as np      
import cv2
import time

## source (raw sram response) and destination (to store generated images) folders

path = '/home/stark/thesis/sram/dataxmc/tflite/dataset/raw-3'
dest_path = '/home/stark/thesis/sram/dataxmc/tflite/dataset/image-3'


## start recording execution time of program
start = time.time()

## fetch raw responses from the source folder (having raw response data under it with board folder names) 
folders = []
for filename in os.listdir(path):
    if filename.startswith('board'):
        folders.append(filename)

## create target folders to save images with same name as source folders
for folder in folders:
    os.mkdir(os.path.join(dest_path,folder))

## processing raw responses
def file_to_image(folder):
  name =[]
  for file in os.listdir(os.path.join(path,folder)):
    name.append(file)
  for file in name:
    if file.startswith('board'):
        f = open(os.path.join(path,folder,file), "rb")
        s =f.read()
        binvalue = list(bytearray(s))

        ## hex to binary conversion and image generation
        new=[]
        for i in binvalue:
          new.append(bin(int(i))[2:].zfill(8))  ## removing 0b prefix
        str1 = ''.join(str(e) for e in new)
        string_2_int =[int(i) for element in str1 for i in element]
        string_2_int = np.array(string_2_int)
        length = int(len(string_2_int)/1024)    
        data_2_img = string_2_int.reshape(length,1024)
        image = Image.fromarray((data_2_img * 255).astype('uint8'), mode ='L')
        new_filename = file.split(' ')[0] + '.png'
        image.save(os.path.join(dest_path,folder,new_filename))        
    
for folder in folders:
    images = file_to_image(folder)


end = time.time()

print("The time of execution of above program is :", end-start)
