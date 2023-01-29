import sys
from keras.models import load_model
from PIL import Image
import numpy as np
import os
# Load the trained model
model = load_model('model.h5')


# Function to predict the class of an image
def predict_image(img_path):
    # Open the image and resize it to 32x32
    img = Image.open(img_path).resize((32, 32))
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Add a dimension to the array to make it (1, 32, 32, 1)
    img_array = np.expand_dims(img_array, axis=0)
    # Normalize the pixel values
    img_array = img_array / 255.0
    # Make predictions
    predictions = model.predict(img_array)
    # Get the class with the highest probability
    class_index = np.argmax(predictions)
    # Get the confidence of the prediction
    confidence = predictions[0][class_index]
    return class_index,confidence

# Get the path to the directory from the command line
dir_path = sys.argv[1]

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    # Get the full path to the file
    file_path = os.path.join(dir_path, filename)
    if os.path.isfile(file_path) and file_path.endswith('.png'):
        prediction,confidence = predict_image(file_path)
        print(f'The predicted class for {filename} is: {prediction} with confidence of {confidence*100:.2f}%')