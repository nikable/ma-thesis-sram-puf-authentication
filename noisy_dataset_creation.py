## based on @reshmi's work https://github.com/reshmisuragani/Master-Thesis-ML-SRAM_PUF
import numpy as np
from skimage.util import random_noise
import cv2
import glob,os
from PIL import Image
import time

## source (intact images) and destination (to store noisy images) folders 
path = '/home/stark/thesis/sram/dataxmc/tflite/intact'
dest_path = '/home/stark/thesis/sram/dataxmc/tflite/noisy'

## start tracking execution time
start = time.time()

# fetching source folders having board response images
folders = []
for filename in os.listdir(path):
    if filename.startswith('board'):
        folders.append(filename)

# creating target folders with same name as source folders
for folder in folders:
    os.mkdir(os.path.join(dest_path,folder))

## adding noise to images
def file_to_image(folder):
  name =[]
  for file in os.listdir(os.path.join(path,folder)):
    name.append(file)
  for file in name:
    if file.startswith('board'):
        img =  cv2.imread(os.path.join(path,folder,file))
        noise_img = random_noise(img, mode='gaussian', mean=0, var=0.05, clip=True)
        noise_img = (255*noise_img).astype(np.uint8)
        image = Image.fromarray(noise_img)
        new_filename = file.split('.png')[0] + 'noise.png'
        image.save(os.path.join(dest_path,folder,new_filename))
    
for folder in folders:
    images = file_to_image(folder)

end = time.time()

print("The time of execution of above program is :", end-start)
