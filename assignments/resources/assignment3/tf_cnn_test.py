from __future__ import absolute_import, division, print_function

import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation
import cv2

# Real-time data preprocessing
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()

# Real-time data augmentation
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=25.)

# Convolutional network building
## To Do. same as before.
    ## Define your network here

# Define model
## To Do
    ## Define model and assign network. Same as training.

# Load Model into model object
## To Do.
    ## Use the model.load() function

# load test images
from tflearn.data_utils import image_preloader
import numpy as np
# Load path/class_id image file:
dataset_file = 'my_dataset.txt'

X_test, Y_test = image_preloader(dataset_file, image_shape=(32, 32), mode='file',
                       categorical_labels=True, normalize=True,
                       files_extension=['.jpg', '.png'], filter_channel=True)
X_test = np.array(X_test)
Y_test = np.array(Y_test)


# predict test images label
y_pred = model.predict(X_test)

# Compute accuracy of trained model on test images
print ("Accuracy: ",np.sum(np.argmax(y_pred, axis=1) == np.argmax(Y_test, axis=1))*100/Y_test.shape[0],"%")
