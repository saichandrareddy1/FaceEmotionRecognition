#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:28:16 2019

@author: saireddy
"""


__author__  = 'Sai Reddy'

import numpy as np
import pandas as pd
import os
import cv2

data = pd.read_csv("/home/saireddy/Desktop/capstone/fer2013/fer2013.csv", delimiter=",")


emotion = data['emotion']
pixels = data['pixels']
Usage = data['Usage']

print(emotion.unique())
print(Usage.unique())

Usage_path = ['Training', 'PublicTest', 'PrivateTest']
for i in range(len(Usage_path)):
	if not os.path.exists(Usage_path[i]):
		os.mkdir(Usage_path[i])
		

#label_path = [0, 1, 2, 3, 4, 5, 6]
label_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

for i in range(len(label_names)):
	if not os.path.exists(os.path.join("/home/saireddy/Desktop/capstone/fer2013/Training/", label_names[i])):
		os.mkdir(os.path.join("/home/saireddy/Desktop/capstone/fer2013/Training/", label_names[i]))
		
	if not os.path.exists(os.path.join("/home/saireddy/Desktop/capstone/fer2013/PublicTest/", label_names[i])):
		os.mkdir(os.path.join("/home/saireddy/Desktop/capstone/fer2013/PublicTest/", label_names[i]))
		
	if not os.path.exists(os.path.join("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/", label_names[i])):
		os.mkdir(os.path.join("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/", label_names[i]))
		
		
label = emotion.values
print(len(label))

images = np.array([np.fromstring(image, np.uint8, sep=' ') for image in pixels])

Usage_ = Usage.values

for i in range(len(label)):
	if label[i] == 0 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Angry/00"+str(i)+'.jpg', img)
		
	if label[i] == 1 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Disgust/00"+str(i)+'.jpg', img)
	
	if label[i] == 2 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Fear/00"+str(i)+'.jpg', img)
	
	if label[i] == 3 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Happy/00"+str(i)+'.jpg', img)
		
	if label[i] == 4 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Sad/00"+str(i)+'.jpg', img)
		
	if label[i] == 5 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Suprise/00"+str(i)+'.jpg', img)
		
	if label[i] == 6 and Usage_[i] == 'Training':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/Training/Neutral/00"+str(i)+'.jpg', img)
		
		


for i in range(len(label)):
	if label[i] == 0 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Angry/00"+str(i)+'.jpg', img)
		
	if label[i] == 1 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Disgust/00"+str(i)+'.jpg', img)
	
	if label[i] == 2 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Fear/00"+str(i)+'.jpg', img)
	
	if label[i] == 3 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Happy/00"+str(i)+'.jpg', img)
		
	if label[i] == 4 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Sad/00"+str(i)+'.jpg', img)
		
	if label[i] == 5 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Suprise/00"+str(i)+'.jpg', img)
		
	if label[i] == 6 and Usage_[i] == 'PublicTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PublicTest/Neutral/00"+str(i)+'.jpg', img)
		
for i in range(len(label)):
	if label[i] == 0 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Angry/00"+str(i)+'.jpg', img)
		
	if label[i] == 1 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Disgust/00"+str(i)+'.jpg', img)
	
	if label[i] == 2 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Fear/00"+str(i)+'.jpg', img)
	
	if label[i] == 3 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Happy/00"+str(i)+'.jpg', img)
		
	if label[i] == 4 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Sad/00"+str(i)+'.jpg', img)
		
	if label[i] == 5 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Suprise/00"+str(i)+'.jpg', img)
		
	if label[i] == 6 and Usage_[i] == 'PrivateTest':
		print(i)
		img = images[i].reshape(48, 48)
		cv2.imwrite("/home/saireddy/Desktop/capstone/fer2013/PrivateTest/Neutral/00"+str(i)+'.jpg', img)