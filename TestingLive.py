import tensorflow as tf
import cv2
import numpy as np

file_path = input('Input Model File Path: ')
model = tf.keras.models.load_model(file_path)

cam = cv2.VideoCapture(1)
cam.set(3, 100)
cam.set(4, 100)

while True:
    _, og = cam.read(0)
    frame = cv2.cvtColor(og, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, dsize = (100,100))
    frame = np.reshape(frame, (1, 100, 100, 1))

    prediction = np.round(model.predict(frame)[0][0])
    print(prediction)
    

