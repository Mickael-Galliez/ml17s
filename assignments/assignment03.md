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

- tensorflow
- tflearn
- h5py
- hdf5
- SciPy

##### Tensorflow
If you have [anaconda](https://www.continuum.io/) installed, then installing tensorflow and tflearn is straightforward. To install tensorflow, activate your conda environment and run the following command.

        conda install tensorflow

Press 'y' when asked for permission. This will install tensorflow and all required packages.

##### tflearn
To install tflearn run the following command in Ubuntu. 'pip' should already be installed on your system.

        pip install tflearn

##### Other packages
You can directly install other packages using anaconda.

        conda install package_name
<!--
#### Note: For Windows
In order to install these packages in anaconda in Windows systems, launch your environment in console or simply launch anaconda console then activate your environment. Now you can install these packages using above commands.

You can install tensorflow in Windows by first creating an environment with python=3.5 then install tensorflow from conda-forge repository. Lastly install tflearn using pip.

        conda create -n my_env python=3.5
        conda install -c conda-forge tensorflow
        pip install tflearn
-->

### Tasks
#### 1. Create, Train and Save a CNN Model:
First task is to use the code from tflearn CNN for CIFAR-10 given at [link](https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py) and modify it according to the following architecture. Run the algorithm for 5 epochs and save the model using the **mode.save('filename')** command at the end of the code. Skeleton code is given in file tf_cnn_train.py.

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

          model.save('filename.tfl')

#### Deliverable Task 1
Provide a screenshot of your simulation after 5 epochs.

#### 2. Load and Refine Model:
In this task you will load the model saved in task 1 and refine it by running for at least 5 more epochs. Compare the results by providing a screenshot of the accuracy. Use the template code in tf_ccn_refine.py file and just add the following line to after you define to model to load the model first and then retrain it.

        model.load(model, 'filename.tfl')

#### Deliverable Task 2
Provide a screenshot of your simulation after retraining the model for at least 5 epochs.


#### 3. Test Model on unseen data:
In this task you will test your trained model on unseen data to see how good it works. We will use 'image_preloader' class from tflearn for this task. Test images are provided in the test_images folder. images_database.txt file contain images path+name and their corresponding label as nominal value on each line separated by space (check the file). You can add more files to the test_images folder by adding file name and its label to images_database.txt file. Labels for CIFAR-10 are given below. Place the file images_database.txt in the same directory as tf_cnn_test.py file which has the skeleton code for this task.  This file will load the model and test images and then find the accuracy of your trained model on these test images. Provide screenshot of your accuracy result.

          - airplane  0
          - car       1
          - bird      2
          - car       3
          - deer      4
          - dog       5
          - frog      6
          - horse     7
          - ship      8
          - truck     9

#### 4. Bonus: Get an accuracy of above 85%
Get an accuracy of above 85% of test images for bonus marks.
