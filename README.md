# SRAM-PUF-Authentication

## This codebase is organized into five modules (feature branches):

* feature/pre-processing: to pre-process the raw dataset before training it with machine learning models
* fearure/model-training: model training with the mobilenetv2 and the efficient-net lite using pre-processed dataset
* feature/authenticator: to process incoming authentication requests and interact with the model for classification
* feature/sender: contains SRAM responses (images) and sends them to the server for authentication
* feature/arduino: to generate SRAM responses on Arduino Uno and calculate the Intra Hamming Distance

### The possible workflow is described below: 

1. Collect the raw dataset:
*  This dataset is provided by TUM and can be found at their **[GitLab repo:](https://gitlab.lrz.de/tueisec/PQAS/-/tree/master/matlab/datasets/SRAMxmc16/data)**
*  It contains the raw SRAM responses collected from 143 XMC microcontroller boards. Each board is sampled 101 times and exported in a ".bin" format. Therefore, each board contains 101 responses. 
*  Dataset uploaded in the above GitLab repo is in the [Git LFS](https://git-lfs.com/) format, so it would take a significant amount of time to pull from the repository.
