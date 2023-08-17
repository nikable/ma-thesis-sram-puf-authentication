import numpy as np
#import tensorflow as tf
# tflite library for edge device
import tflite_runtime.interpreter as tflite

# Load TFLite model and allocate tensors.
# EfficcientNet-Lite model
interpreter = tflite.Interpreter(model_path="/home/pi1/tflite/SRAM-PUF-AUTH/authenticator/efficientnet/noisy/model.tflite")
# Custom model (converted from Keras API)
#interpreter = tflite.Interpreter(model_path="model50.tflite")

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_shape = input_details[0]['shape']
output_shape = output_details[0]['shape']

print("following is the input shape of the model")
print(input_shape)

interpreter.allocate_tensors()

# input details
print("model input metadata")
print(input_details)
# output details
print("model output metadata")
print(output_details)
