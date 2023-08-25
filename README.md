### Authentication module

This module interacts with the ML model and authenticates incoming SRAM responses (images).

### Possible workflow of this module is described below:
1. Deploying models on the device:
*  Export the trained efficient-net lite and mobilenetv2 models in the *"tflite"* format (included in the model training notebooks in the repo) and place them on the authenticator device (one of the Raspberry Pis).
*  Prepare Python and TFlite runtime on the device.
*  Pre-trained models are exported and deployed in the *authenticator/efficientnet* and *authenticator/mobilenet* directories (can be seen in the repo). Each model is trained for a specific use case (intact, noisy, and corrupted images) and exported in the above-mentioned directories. 
  
2. Run model inference depending upon the use case:
* This module contains six Python server submodules (3 use cases x 2 models), which will interact with the respective model depending upon the received incoming authentication request coming from a device.
* Inference submodule is organized in the *authenticator/inference* directory.



