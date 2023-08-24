### based on @reshmi's work https://github.com/reshmisuragani/Master-Thesis-ML-SRAM_PUF
import os,glob
import random
from itertools import cycle,islice
from PIL import Image
import numpy as np      
import numpy
import cv2
import time

## source dataset folder (containing raw sram response folders)
path = '/home/stark/thesis/sram/dataxmc/tflite/dataset/corrupted-dataset/raw-3'

## corrupted 20%
dest_path = '/home/stark/thesis/sram/dataxmc/tflite/dataset/corrupted-dataset/corrupted'

## start timer
start = time.time()

## fetching source raw responses from folder (starting with name board)
folders = []
for filename in os.listdir(path):
    if filename.startswith('board'):
        folders.append(filename)

## creating target folders to save corrupted images with same name as source folders
for folder in folders:
    os.mkdir(os.path.join(dest_path,folder))

## generating corrupted images from each raw response file
def file_to_image(folder):
  name =[]
  for file in os.listdir(os.path.join(path,folder)):
    name.append(file)
  for file in name:
    if file.startswith('board'):
        f = open(os.path.join(path,folder,file), "rb")
        s = f.read()
        binvalue = list(bytearray(s))
        n  = int(len(binvalue)*0.20) # percentage of bits to be corrupted
        binvalue[-n:] = [0] * n # corrupt from bottom
        # binvalue[:n] = [0] * n # corruot from top if required
        
        # hex to binary conversion and image generation
        new=[]
        for i in binvalue:
            new.append(bin(int(i))[2:].zfill(8))
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
