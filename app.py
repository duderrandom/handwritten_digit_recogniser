import tkinter as tk
from tkinter import Canvas, Button, Label
import numpy as np
from PIL import Image, ImageDraw, ImageOps
import tensorflow as tf
class DigitRecognizerApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Handwritten Digit Recognizer")
        self.model=tf.keras.models.load_model('mnist_cnn_model.h5')
        self.canvas=Canvas(root,width=200,height=200,bg='white')
        self.canvas.pack(pady=10)
        self.image=Image.new("L",(200,200),255)
        self.draw=ImageDraw.Draw(self.image)
        self.canvas.bind("<B1-Motion>",self.paint)
        Button(root,text="Predict",command=self.predict).pack(side=tk.LEFT,padx=10)
        Button(root,text="Clear",command=self.clear).pack(side=tk.RIGHT,padx=10)
        self.result_label=Label(root,text="Draw a digit",font=('Arial',16))
        self.result_label.pack(pady=10)
    def paint(self,event):
        x1,y1=(event.x-8),(event.y-8)
        x2,y2=(event.x+8),(event.y+8)
        self.canvas.create_oval(x1,y1,x2,y2,fill='black',width=0)
        self.draw.ellipse([x1,y1,x2,y2],fill=0)
    def clear(self):
        self.canvas.delete("all")
        self.image=Image.new("L",(200,200),255)
        self.draw=ImageDraw.Draw(self.image)
        self.result_label.config(text="Draw a digit")
    def predict(self):
        img=self.image.resize((28,28))
        img=ImageOps.invert(img)
        img=np.array(img).astype('float32')/255.0
        img=img.reshape(1,28,28,1)
        pred= self.model.predict(img)[0]
        digit=np.argmax(pred)
        confidence=pred[digit]*100
        self.result_label.config(
            text=f"Prediction:{digit}\nConfidence:{confidence:.1f}%"
        )
if __name__=="__main__":
    root=tk.Tk()
    app=DigitRecognizerApp(root)
    root.mainloop()