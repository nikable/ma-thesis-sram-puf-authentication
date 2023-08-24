# Model training

This module focuses on training efficientnet-lite and mobilenet models with intact, noisy and corrupted dataset. We use TFLite Model maker library to train models.

## Training on the Google Colab
*  The python runtime is updated from 3.9 to 3.10 on the Google Colab, which is not compatible with the TFLite Model Maker [more details](https://discuss.tensorflow.org/t/tflite-model-maker-installation/16577/21). 
*  Current alternative is setting up the TensorFlow environment dependencies on the local system and train models. 
*  Since our data set is small to start with (3 boards; 303 images), this is doable on the local system.

## Training on the local system
*  This can be done by setting up a [miniconda environment](https://docs.conda.io/en/latest/miniconda.html) depending on your local system operating system. 
*  A python virtual environment can be created with the version 3.9 to make the setup compatible with the TFLite Model Maker. 
*  Make sure to lower the numpy version as well (<1.24) to make it with the TFLite Model maker [more details](https://discuss.tensorflow.org/t/tensorflow-lite-model-maker-import-errors/14896).


## Overview of the training phase
*  3 types of dataset including intact, noisy and corrupted would be trained with both, Efficient-Net Lite and MobileNetV2 models. 
*  Jupyter notebook is created for each type (total 6 notebooks 3 * 2)
*  Images should be used in the RGB format to be able to work with the TFLite Model Maker (as of now).
