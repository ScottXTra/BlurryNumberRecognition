# BlurryNumberRecognition

 Recognizing blurry numbers from images using a neural network. 

# Generate Data
Create training data (This may take 5 mins depending on IO speed and CPU)

    python3 generate_images.py

# Training

It may take a few tries to get the training to work.

    python3 train_network.py

![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/training.png?raw=true)

# Predict Using Unseen Data
Test the model on unseen data 

    python3 predict.py data/test/<number 1 - 9>
    Example python3 predict.py data/test/4
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/prediction_on_unseen_data.png?raw=true)
