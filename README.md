Handwritten Digit Recognition System
A desktop application that recognizes handwritten digits (0-9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Users can draw digits on a Tkinter canvas and get real-time predictions with confidence scores.


Features

CNN Model: Trained on MNIST dataset with convolutional, pooling, dropout, and dense layers.
Tkinter GUI: Interactive canvas for freehand drawing with Predict and Clear buttons.
Image Processing: Automatic preprocessing of drawings to match MNIST format (28x28 grayscale, normalized).
Real-time Prediction: Instant digit recognition with confidence percentage display.
Clean & Simple: Minimal dependencies and straightforward workflow.


Files

train_cnn.py - Trains and saves the CNN model (mnist_cnn_model.h5)
app.py - Tkinter GUI application for drawing and prediction
requirements.txt - Python dependencies
README.md - This file


Requirements
Python 3.x
TensorFlow >= 2.0.0
Pillow >= 8.0.0
NumPy >= 1.18.0
Tkinter (usually included with Python)


Installation
Clone or download this repository
Install dependencies:
pip install -r requirements.txt


Usage
1. Train the Model
First, train the CNN on the MNIST dataset:

python train_cnn.py
This will download MNIST, train the model for 5 epochs, and save it as mnist_cnn_model.h5.

2. Launch the Application
python app.py

3. Use the Application
Draw a digit (0-9) on the white canvas using your mouse
Click "Predict" to see the recognized digit and confidence percentage
Click "Clear" to erase the canvas and try another digit


Model Architecture
The CNN consists of:

Conv2D (32 filters, 3x3, ReLU) → MaxPooling2D
Conv2D (64 filters, 3x3, ReLU) → MaxPooling2D
Flatten → Dense (64 units, ReLU) → Dropout (0.5)
Dense (10 units, Softmax) for class probabilities


How It Works

User draws digit on Tkinter canvas
Canvas content is saved as PIL Image
Image is resized to 28x28, converted to grayscale, inverted (black-on-white → white-on-black like MNIST)
Pixel values normalized to [0,1] range
Image reshaped to (1, 28, 28, 1) for CNN input
Model predicts digit class and confidence
Result displayed in GUI: "Prediction: X\nConfidence: Y.Y%"


Notes

The first run requires internet to download MNIST dataset (~11 MB)
Training takes approximately 30-60 seconds on a modern CPU
The GUI canvas is 200x200 pixels but drawings are automatically scaled to 28x28
For best results, draw digits similar to MNIST style (centered, moderate thickness)


License

This project is provided as-is for educational and personal use.


Acknowledgments
MNIST dataset (Yann LeCun et al.)
TensorFlow/Keras team
Tkinter for Python GUI# handwritten_digit_recogniser
