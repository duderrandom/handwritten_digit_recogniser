# ✍️ Handwritten Digit Recogniser

A simple desktop application that uses a **Convolutional Neural Network (CNN)** to recognize handwritten digits from **0–9**.

The application provides an interactive **Tkinter drawing canvas** where users can draw a digit with their mouse and receive an immediate prediction along with the model's confidence score.

> **Built with Python, TensorFlow/Keras, NumPy, Pillow, and Tkinter.**

---

## ✨ Features

* 🧠 **CNN-based Recognition** — Neural network trained on the MNIST handwritten digit dataset.
* 🖌️ **Interactive Drawing Canvas** — Draw digits directly using your mouse.
* ⚡ **Real-Time Prediction** — Get predictions almost instantly.
* 📊 **Confidence Score** — Displays the model's predicted probability.
* 🖼️ **Automatic Image Processing** — Converts drawings into MNIST-compatible `28×28` grayscale images.
* 🧹 **Clear & Redraw** — Easily erase the canvas and test another digit.
* 📦 **Simple Setup** — Minimal dependencies and straightforward project structure.

---

## 🖥️ Demo

The application follows a simple workflow:

```text
┌─────────────────────────────┐
│     Handwritten Digit       │
│       Recogniser            │
│                             │
│     ┌─────────────────┐     │
│     │                 │     │
│     │    Draw Here    │     │
│     │       7         │     │
│     │                 │     │
│     └─────────────────┘     │
│                             │
│   [ Predict ]   [ Clear ]   │
│                             │
│   Prediction: 7             │
│   Confidence: 98.7%         │
└─────────────────────────────┘
```

---

## 🧠 Model Architecture

The recognition model is a **Convolutional Neural Network (CNN)** designed for image classification.

### Architecture

```text
Input Image
   │
   ▼
28 × 28 × 1
   │
   ▼
Conv2D
32 Filters, 3×3, ReLU
   │
   ▼
MaxPooling2D
   │
   ▼
Conv2D
64 Filters, 3×3, ReLU
   │
   ▼
MaxPooling2D
   │
   ▼
Flatten
   │
   ▼
Dense
64 Units, ReLU
   │
   ▼
Dropout
0.5
   │
   ▼
Dense
10 Units, Softmax
   │
   ▼
Digit Prediction (0–9)
```

### Why CNN?

CNNs are particularly effective for image recognition because convolutional layers can learn spatial patterns such as:

* Edges
* Curves
* Lines
* Shapes
* Digit-specific features

The final **Softmax layer** produces probabilities for all ten possible digits.

---

## 🔄 How It Works

The application converts the user's drawing into the same general format used by the MNIST model.

### 1. Draw

The user draws a digit on the Tkinter canvas.

### 2. Capture

The canvas contents are converted into a PIL image.

### 3. Preprocess

The image is:

1. Resized to **28×28 pixels**
2. Converted to **grayscale**
3. Inverted to match the MNIST format
4. Normalized to pixel values between **0 and 1**
5. Reshaped into the CNN input format:

```text
(1, 28, 28, 1)
```

### 4. Predict

The trained CNN processes the image and produces probabilities for digits `0–9`.

### 5. Display

The application selects the digit with the highest probability and displays:

```text
Prediction: 7
Confidence: 98.7%
```

---

## 📂 Project Structure

```text
handwritten_digit_recogniser/
│
├── app.py                  # Tkinter GUI and digit prediction
├── train_cnn.py            # CNN training script
├── requirements.txt        # Python dependencies
├── mnist_cnn_model.h5      # Trained CNN model
└── README.md               # Project documentation
```

> `mnist_cnn_model.h5` is generated automatically when the training script is executed.

---

## ⚙️ Requirements

Make sure you have:

* **Python 3.x**
* **TensorFlow >= 2.0**
* **Pillow >= 8.0**
* **NumPy >= 1.18**
* **Tkinter** — usually included with standard Python installations

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd handwritten_digit_recogniser
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

Before launching the application, train the CNN:

```bash
python train_cnn.py
```

The training script will:

1. Download the **MNIST dataset**
2. Preprocess the training and test images
3. Build the CNN
4. Train the model for **5 epochs**
5. Save the trained model as:

```text
mnist_cnn_model.h5
```

Depending on your system, training should take approximately **30–60 seconds on a modern CPU**.

---

## ▶️ Run the Application

Once the model has been trained:

```bash
python app.py
```

Then:

1. Draw a digit from **0–9** on the canvas.
2. Click **Predict**.
3. View the predicted digit and confidence score.
4. Click **Clear** to try another digit.

---

## 🖼️ Image Processing Pipeline

The application's preprocessing pipeline can be summarized as:

```text
User Drawing
     │
     ▼
Tkinter Canvas
     │
     ▼
PIL Image
     │
     ▼
Resize to 28×28
     │
     ▼
Convert to Grayscale
     │
     ▼
Invert Colors
     │
     ▼
Normalize Pixels
     │
     ▼
Reshape → (1, 28, 28, 1)
     │
     ▼
      CNN
     │
     ▼
Prediction + Confidence
```

This preprocessing is important because the model expects input similar to the images it encountered during MNIST training.

---

## 📊 Dataset

This project uses the **MNIST Handwritten Digit Dataset**, a widely used benchmark dataset for image classification.

The dataset contains grayscale images of handwritten digits from `0` through `9`.

Each image has a resolution of:

```text
28 × 28 pixels
```

The dataset is automatically downloaded by TensorFlow/Keras during training.

---

## 💡 Tips for Better Predictions

For the best results:

* Draw digits roughly in the **center** of the canvas.
* Use a **moderate stroke thickness**.
* Avoid drawing extremely small digits.
* Try to imitate the general writing style found in MNIST.
* Make sure the complete digit is visible on the canvas.
* Avoid additional marks or multiple digits.

The model may occasionally make incorrect predictions, particularly for digits that are visually similar, such as:

```text
3 ↔ 8
4 ↔ 9
5 ↔ 6
7 ↔ 1
```

---

## 🛠️ Technologies Used

| Technology             | Purpose                        |
| ---------------------- | ------------------------------ |
| **Python**             | Core programming language      |
| **TensorFlow / Keras** | CNN development and training   |
| **MNIST**              | Training dataset               |
| **NumPy**              | Numerical and array operations |
| **Pillow**             | Image processing               |
| **Tkinter**            | Desktop graphical interface    |

---

## 📌 Future Improvements

Some possible improvements for future versions:

* [ ] Display the top-3 predictions
* [ ] Add prediction probability bars
* [ ] Improve automatic digit centering and scaling
* [ ] Add keyboard shortcuts
* [ ] Add model accuracy/loss graphs
* [ ] Support touch/stylus input
* [ ] Add dark/light UI themes
* [ ] Improve preprocessing for thicker/thinner handwriting
* [ ] Package the application as a standalone executable
* [ ] Add a test mode with randomly selected MNIST samples

---

## 📚 Learning Objectives

This project demonstrates several fundamental concepts in machine learning and software development:

* Convolutional Neural Networks
* Image classification
* Supervised learning
* Dataset preprocessing
* Image normalization
* Model training and inference
* GUI development with Tkinter
* Connecting an ML model to a desktop application

---

## 📄 License

This project is provided **as-is for educational and personal use**.

---

## 🙏 Acknowledgments

* **MNIST Dataset** — Yann LeCun and collaborators
* **TensorFlow/Keras** — Machine learning framework
* **Tkinter** — Python's standard GUI toolkit
* **Pillow** — Python Imaging Library

---

### ⭐ If you found this project useful

Feel free to **star the repository**, experiment with the model, and improve the application!
