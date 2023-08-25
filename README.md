# Data pre-processing module

This module focuses on generating image dataset from raw SRAM content and pre-processing them depending on the task. Each pre-processing file would look for a source folder containing either responses or images (depending on the task), generate a target folder, and put processed data in the same.

*  file\_to\_image: this will generate intact grayscale images from raw responses
*  data\_corruption: corrupting bottom part of the dataset (customization explained in code)
*  noisy\_dataset\_creation: add gaussian noise to the dataset
*  grayscale\_to\_rgb\_converter: generate RGB dataset from grayscale images to train with the TensorFlow Lite model maker  
