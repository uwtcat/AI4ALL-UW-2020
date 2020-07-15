#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from sklearn import datasets, neighbors
import matplotlib.pyplot as plt

cs = ColorSensor()
btn = Button()
sound = Sound()

# Data import and manipulation
# Load the digits data set
digits = datasets.load_digits()

# Extract the input data, force values to be between 0.0 and 1.0
X_digits = digits.data / digits.data.max()

# Extract the true values for each sample (each a digit between 0-9)
y_digits = digits.target

# Extract training data, 90% of total data
n_samples = len(X_digits)
train_test_split = int(.9*n_samples)

# Partition training set
X_train = X_digits[:train_test_split]
y_train = y_digits[:train_test_split]
X_test = X_digits[train_test_split:]
y_test = y_digits[train_test_split:]

# ML function

# Import the default K-Nearest Neighbors classifier
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# Train the classifer
knn.fit(X_train, y_train)

n = 7

while not btn.any(): # While no (not any) button is pressed.
    sleep(0.01)  # Wait 0.01 second

sound.beep()
if cs.color == 2:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 0

elif cs.color == 3:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 1

elif cs.color == 4:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 2

elif cs.color == 5:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 3

elif cs.color == 7:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 4

elif cs.color == 1:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 5

elif cs.color == 6:
    sound.beep()
    #sound.speak(cs.color_name)
    n = 6

else:
    sound.speak('No color detected')

#Classifier output 
y_pred = knn.predict(X_test.data)

sound.speak(y_pred)