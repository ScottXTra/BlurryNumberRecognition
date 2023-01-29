# BlurryNumberRecognition

 Recognizing blurry numbers from images using a neural network. 
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/0/0_11.png?raw=true)
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/1/1_11.png?raw=true)
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/2/2_11.png?raw=true)
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/3/3_11.png?raw=true)
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/4/4_11.png?raw=true)
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/5/5_11.png?raw=true)
![enter image description here](https://github.com/ScottXTra/BlurryNumberRecognition/blob/master/data/test/6/6_11.png?raw=true)
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
