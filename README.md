# Data pre-processing module

This module focuses on generating image dataset from raw sram content and pre-process them depending on the task.

*  file\_2\_image: this will generate intact grayscale images from raw responses
*  data\_corruption: corrupting bottom part of the dataset (customization explained in code)
*  noisy\_dataset\_creation: add guassian noise to the dataset
*  grayscale\_to\_rgb\_converter: generate RGB dataset from grayscale images to train with the TensorFlow Lite model maker  
