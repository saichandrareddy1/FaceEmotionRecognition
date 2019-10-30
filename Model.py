#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:51:47 2019

@author: saireddy
"""

__author__ = 'Sai Reddy'

from keras.layers import Conv2D, MaxPool2D, Dense, Flatten
from keras.layers import BatchNormalization
from keras.layers import Dropout, ZeroPadding2D
from keras.optimizers import Adam, SGD, RMSprop
from keras.preprocessing import image
from keras.models import Sequential
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
import numpy as np


def data_prep():
	
	train_gen = image.ImageDataGenerator(rescale = 1./255,
                                    featurewise_center=True, 
                                    samplewise_center=True, 
                                    featurewise_std_normalization=True, 
                                    samplewise_std_normalization=True, 
                                    zca_whitening=False, zca_epsilon=1e-06, 
                                    rotation_range=10, width_shift_range=0.0,
                                    height_shift_range=0.0, brightness_range=(0.2, 0.2),
                                    shear_range=0.2, zoom_range=0.2, 
                                    channel_shift_range=0.0, fill_mode='nearest', 
                                    cval=0.0, horizontal_flip=True, vertical_flip=True,
									data_format=None, validation_split=0.0, dtype=None)
	
	test_gen = image.ImageDataGenerator(rescale = 1./255,
                                    featurewise_center=True, 
                                    samplewise_center=True, 
                                    featurewise_std_normalization=True, 
                                    samplewise_std_normalization=True, 
                                    zca_whitening=False, zca_epsilon=1e-06, 
                                    rotation_range=10, width_shift_range=0.0,
                                    height_shift_range=0.0, brightness_range=(0.2, 0.2),
                                    shear_range=0.2, zoom_range=0.2, 
                                    channel_shift_range=0.0, fill_mode='nearest', 
                                    cval=0.0, horizontal_flip=True, vertical_flip=True,
									data_format=None, validation_split=0.0, dtype=None)
	
	val_gen = image.ImageDataGenerator(rescale = 1./255,
                                    featurewise_center=True, 
                                    samplewise_center=True, 
                                    featurewise_std_normalization=True, 
                                    samplewise_std_normalization=True, 
                                    zca_whitening=False, zca_epsilon=1e-06, 
                                    rotation_range=10, width_shift_range=0.0,
                                    height_shift_range=0.0, brightness_range=(0.2, 0.2),
                                    shear_range=0.2, zoom_range=0.2, 
                                    channel_shift_range=0.0, fill_mode='nearest', 
                                    cval=0.0, horizontal_flip=True, vertical_flip=True,
									data_format=None, validation_split=0.0, dtype=None)
	
	
	train_data = train_gen.flow_from_directory("/home/saireddy/Desktop/capstone/fer2013/images/Training/",
                                           target_size = (48, 48),
                                           classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'],
                                           class_mode = 'categorical',
                                           batch_size = 32,seed = 1,
										   color_mode = "grayscale")
	
	test_data = test_gen.flow_from_directory("/home/saireddy/Desktop/capstone/fer2013/images/PublicTest/",
                                           target_size = (48, 48),
                                           classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'],
                                           class_mode = 'categorical',
                                           batch_size = 32,seed = 1,
										   color_mode = "grayscale")
	
	val_data = val_gen.flow_from_directory("/home/saireddy/Desktop/capstone/fer2013/images/PrivateTest/",
                                           target_size = (48, 48),
                                           classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'],
                                           class_mode = 'categorical',
                                           batch_size = 32,seed = 1,
										   color_mode = "grayscale")
	
	return train_data, test_data, val_data


def model_creation():
	
	model = Sequential()
	
	model.add(Conv2D(2, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
				  input_shape= (48, 48, 1),activation = 'relu')) ##Input Layers
	
	model.add(Conv2D(2, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	model.add(BatchNormalization(axis = -1))
	model.add(MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding = 'SAME')) #Max Pool1
	model.add(Dropout(0.5))
	
	
	model.add(ZeroPadding2D(padding = (2, 2)))
	model.add(Conv2D(3, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	
	model.add(Conv2D(3, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	
	model.add(MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding = 'SAME')) #MaxPool2
	model.add(Dropout(0.5))
	
	model.add(ZeroPadding2D(padding = (2, 2)))
	model.add(Conv2D(7, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	
	model.add(Conv2D(7, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	model.add(BatchNormalization(axis = -1))
	model.add(MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding = 'SAME')) #MaxPool3
	model.add(Dropout(0.5))
	
	
	model.add(ZeroPadding2D(padding = (2, 2)))
	model.add(Conv2D(10, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	
	model.add(Conv2D(10, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	
	model.add(MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding = 'SAME')) #MaxPool4
	model.add(Dropout(0.5))
	
	"""model.add(ZeroPadding2D(padding = (2, 2)))
	model.add(Conv2D(15, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	
	model.add(Conv2D(15, kernel_size=(3, 3), strides=(1, 1), padding='SAME',
activation = 'relu'))
	model.add(BatchNormalization(axis = -1))
	model.add(MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding = 'SAME')) #MaxPool5
	model.add(Dropout(0.5))
	"""
	
	model.add(Flatten())
	
	
	#Dense1
	model.add(Dense(200, activation='relu'))
	model.add(BatchNormalization(axis = -1))
	model.add(Dropout(0.5))
	
	#Dense2
	model.add(Dense(140, activation='relu'))
	model.add(BatchNormalization(axis = -1))
	model.add(Dropout(0.5))
	
	#Dense3
	model.add(Dense(100, activation='relu'))
	model.add(BatchNormalization(axis = -1))
	model.add(Dropout(0.5))
	
	#Dense4
	model.add(Dense(64, activation='relu'))
	model.add(Dropout(0.5))
	
	model.add(Dense(7, activation='softmax'))
	model.summary()
	

	return model

def Training_data(model, train_data, test_data, val_data):
	
	#Optimizers
	Ad = SGD(lr = 0.001)
	
	
		
	#Compile Model
	model.compile(optimizer = Ad,
			   loss = 'categorical_crossentropy',metrics=['accuracy'])
	
	#Fitting Model
	history = model.fit_generator(train_data, steps_per_epoch=10,
							   epochs=100, validation_data=val_data,
							   validation_steps=5)
		
	return history

def test_model(model, test_data):
	score  = model.evaluate_generator(test_data, 
                                  steps = 5)


	#printAccuracy
	print("Accuracyloss:-", score[0])
	print("AccuracyScore",score[1] )
	
	model.save("/home/saireddy/Desktop/capstone/finalweights.h5")
	return score[0], score[1]

def plotting(history):
	
	import matplotlib.pyplot as plt
	print(history.history.keys())
	# summarize history for accuracy
	plt.plot(history.history['acc'])
	plt.plot(history.history['val_acc'])
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()
	
	
	# summarize history for loss
	plt.plot(history.history['loss'])
	plt.plot(history.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()



	
if __name__ == "__main__":
	data = data_prep()
	train_data, test_data, val_data = data
	
	model = model_creation()
	
	history = Training_data(model, train_data, test_data, val_data)
	
	plotting(history)
	
	score = test_model(model, test_data)