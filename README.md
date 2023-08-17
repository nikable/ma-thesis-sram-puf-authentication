# SRAM-PUF-Authentication

This codebase is organized into five modules (feature branches):

* feature/pre-processing: to pre-process the dataset before training
* fearure/model-training: model training with the mobilenetv2 and efficient-net lite
* feature/authenticator: to manage incoming authentication requests and interact with the model for classification
* feature/sender: contains SRAM-responses (images) and sends them to server for authentication
* feature/arduino: to generate SRAM responses on Arduino Uno and calculate the Intra Hamming Distance 
