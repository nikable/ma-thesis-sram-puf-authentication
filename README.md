# SRAM-PUF-Authentication

### This codebase is organized into five modules (feature branches):

* feature/pre-processing: to pre-process the raw dataset before training it with machine learning models
* feature/model-training: model training with the mobilenetv2 and the efficient-net lite using pre-processed dataset
* feature/authenticator: to process incoming authentication requests and interact with the model for classification
* feature/sender: contains SRAM responses (images) and sends them to the server for authentication
* feature/arduino: to generate SRAM responses on Arduino Uno and calculate the Intra Hamming Distance

### The possible workflow is described below: 

1. Collect the raw dataset:
*  This dataset is provided by TUM and can be found at their [GitLab repo](https://gitlab.lrz.de/tueisec/PQAS/-/tree/master/matlab/datasets/SRAMxmc16/data).
*  It contains the raw SRAM responses collected from 143 XMC microcontroller boards. Each board is sampled 101 times and exported in a <em>".bin"</em> format. Therefore, each board contains 101 responses. 
*  Dataset uploaded in the above GitLab repo is in the [Git LFS](https://git-lfs.com/) format, so it would take a significant amount of time to pull from the repository. Ensure you have pulled the complete dataset (containing responses of 143 boards.

2. Pre-process the raw dataset:
*  This includes generating images from the raw SRAM data, and corrupting the dataset, adding noise to the dataset as and when required.
*  Additionally, it also contains a submodule to convert Grayscale images to RGB (requirement from TFLite Model maker; as of now) for model training and execution.

3. Model training:
*  MobileNetV2 and EfficientNet-Lite model training with the intact, corrupted, and noisy dataset (pre-processed in the above module).

4. Authenticator and Sender:
*  Transfering pre-trained models (above module) to the Authenticator (possibly a Raspberry Pi device).
*  Transferring pre-processed images to another device, termed as a sender.
*  Authenticator can then receive images and send them to the pre-trained model for classification.

5. Generating responses from Arduino Uno:
*  Burning the bootloader on the Arduino Uno to reset the board.
*  Generate SRAM responses and view them on a serial output.


