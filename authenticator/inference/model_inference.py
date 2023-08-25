# Imports
from tflite_support.task import vision
from tflite_support.task import core
from tflite_support.task import processor

def classify_image(model_path,image):

    # Initialization
    #base_options = core.BaseOptions("/home/pi1/tflite/model3/mobilenet/model.tflite")
    base_options = core.BaseOptions(model_path)
    
    classification_options = processor.ClassificationOptions(max_results=2)
    options = vision.ImageClassifierOptions(base_options=base_options, classification_options=classification_options)
    classifier = vision.ImageClassifier.create_from_options(options)
    
    
    # Run inference
    image = vision.TensorImage.create_from_file(image)
    classification_result = classifier.classify(image)
    #print(dir(classification_result))
    #print(classification_result.classifications[0].categories[0].score)
    
    # get the first predicted class from the possible predicted classes
    score = classification_result.classifications[0].categories[0].score
    label = classification_result.classifications[0].categories[0].category_name
    
    return score,label
   # print("Classification score:", score , "Board label for image:", label)
