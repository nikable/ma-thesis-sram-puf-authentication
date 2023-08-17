# Imports
from tflite_support.task import vision
from tflite_support.task import core
from tflite_support.task import processor

# Initialization
base_options = core.BaseOptions("model.tflite")

classification_options = processor.ClassificationOptions(max_results=2)
options = vision.ImageClassifierOptions(base_options=base_options, classification_options=classification_options)
classifier = vision.ImageClassifier.create_from_options(options)

# Alternatively, you can create an image classifier in the following manner:
# classifier = vision.ImageClassifier.create_from_file(model_path)

# Run inference
#image = vision.TensorImage.create_from_file("board002Acycle0064_rgb.png")
#image = vision.TensorImage.create_from_file("board000Bcycle0007_rgb.png")
image = vision.TensorImage.create_from_file("board003Dcycle0055_rgb.png")

classification_result = classifier.classify(image)
print(classification_result)

