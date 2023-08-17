import numpy as np
from skimage.util import random_noise
import cv2
import glob,os
from PIL import Image

import time

start = time.time()

#path = r'D:\Uni-passau\thesis-smalldataset\gaussian-50\train'
#dest_path = r"D:\Uni-passau\thesis-smalldataset\gaussian-50\train"
path = '/home/stark/thesis/sram/dataxmc/random/bin-to-image-50'
dest_path = '/home/stark/thesis/sram/dataxmc/random/noisy-50'


# list all folders in a directary
folders = []
for filename in os.listdir(path):
    if filename.startswith('board'):
        folders.append(filename)

# creating target folders
for folder in folders:
    os.mkdir(os.path.join(dest_path,folder))
    
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