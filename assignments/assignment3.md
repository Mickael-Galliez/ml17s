---
layout: page
title: Assignment 3: Convolutional Neural network (CNN) for image classification
permalink: /assignments/assignment3/
---

### Introduction
In this assignment we will train a [Convolutional Neural Network (CNN)](http://cs231n.github.io/convolutional-networks/) on [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset that has 10 distinct classes and around 50,000 images using [tflearn](http://tflearn.org/) and [tensorflow](https://www.tensorflow.org/). The aim is to understand different layers of CNN and how to use tflearn to train a CNN to classify images. Save and load the trained model. And use the trained model to evaluate the accuracy of the model on test images.

<div class='fig figcenter'>
  <img src='images/cnn.jpg'>
</div>

### CIFAR-10 dataset
CIFAR-10 has 60,000 images (50,000 training and 10,000 test images) of 10 different categories (airplane, car/automobile, bird, cat, deer, dog, frog, horse, sheep, truck). Each image in CIFAR-10 has dimension 32x32x3 with width and height equal to 32 and 3 channels (red, green and blue).

### Installing Tensorflow and tflearn
If you have [anaconda]() installed, then installing tensorflow and tflearn is straightforward. To install tensorflow, activate your conda environment and run the following command.
'''
conad install tensorflow
'''

### Tasks
1. First task is to use the code from tflearn CNN for CIFAR-10 given at [link](https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py) and modify it according to the following architecture. Run the algorithm for 5 epochs and save the model using the **mode.save('filename')** command at the end of the code.

#### Layers
  1. Conv: 64 filters of size 3x3 with ReLU activation
  2. Pooling: with filter size 2x2
  3. Conv: 32 filters of size 3x3 with ReLU activation
  4. Pooling: with filter size 2x2
  5. Conv: 32 filters of size 3x3 with ReLU activation
  6. Pooling: with filter size 2x2
  7. Fully Connected: with 256 neurons and ReLU activation and dropout with probability 0.75
  8. Fully Connected: with 256 neurons and ReLU activation and dropout with probability 0.75
  9. Fully Connected output layer: with 10 neurons (equal to number of classes) and softmax classifier.

#### Estimator
Use a logistic regression estimator with gradient descent optimize = ‘adam’,  loss function =  ‘categorical_crossentropy’ and learning rate = 0.01

#### Training
Train the model with a batch size of 64 and run it for at least 5 epochs (number of iterations over the whole training dataset) in first training phase.

#### Save Model
Save the model by inserting the following command at the end of the code.
'''
model.save('filename')
'''

Installing and running IPython is easy. From the command line, the following
will install IPython:

```
pip install "ipython[notebook]"
```

Once you have IPython installed, start it with this command:

```
ipython notebook
```
