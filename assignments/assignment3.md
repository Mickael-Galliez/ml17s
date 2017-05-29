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

### Installing Dependencies
You need the following packages installed. It will install all other packages needed for this assignment.
- SciPy
- tensorflow
- tflearn

##### Tensorflow
If you have [anaconda](https://www.continuum.io/) installed, then installing tensorflow and tflearn is straightforward. To install tensorflow, activate your conda environment and run the following command.

        conda install tensorflow

Press 'y' when asked for permission. This will install tensorflow and all required packages.

##### SciPy
You can directly install scipy using anaconda.

        conda install scipy

##### tflearn
To install tflearn run the following command in Ubuntu. 'pip' should already be installed on your system.

        pip install tflearn.


### Tasks
#### 1. Create, Train and Save a CNN Model:
First task is to use the code from tflearn CNN for CIFAR-10 given at [link](https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py) and modify it according to the following architecture. Run the algorithm for 5 epochs and save the model using the **mode.save('filename')** command at the end of the code.

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
Use a logistic regression estimator with gradient descent optimizer = ‘adam’,  loss function =  ‘categorical_crossentropy’ and learning rate = 0.01

#### Training
Train the model with a batch size of 64 and run it for at least 5 epochs (number of iterations over the whole training dataset) in first training phase.

#### Save Model
Save the model by inserting the following command at the end of the code.

          ```
          model.save('filename.tfl')
          ```
#### Deliverable Task 1
Provide a screenshot of your simulation after 5 epochs.

#### 2. Load and Refine Model:
In this task you will load the model saved in task 1 and refine it by running for at least 5 more epochs. Compare the results by providing a screenshot of the accuracy. Use the template code in tf_ccn_refine.py file and just add the following line to after your define to model to load the model first and then retrain it.

        model.load(model, 'filename.tfl')

#### 3. Test Model on unseen data:
In this task you will test your trained model on unseen data to see how good it works. Test images are provided in the test_images folder. Place the file images_database.txt in the same directory as tf_cnn_test.py file. This file will load the model and test images and then find the accuracy of your trained model on these test images. Provide screenshot of your accuracy result.

#### 4. Bonus: Get an accuracy of above 85%
Get an accuracy of above 85% of test images for bonus marks.
