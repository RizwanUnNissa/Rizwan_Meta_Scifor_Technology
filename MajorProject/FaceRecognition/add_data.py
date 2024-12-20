import face_recognition as fr
import pickle 
import cv2
import sys
from model import load_data
import os

path = 'dataset.pkl'

path_dataset = os.path.abspath(path)


def get_data(name, image):

	data = load_data()
	
	image = fr.load_image_file(image)

	idx = len(data)

	encoding = fr.face_encodings(image)[0]

	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	data[idx]['image'] = image
	data[idx]['name'] = name
	data[idx]['Id'] = idx - 1
	data[idx]['encoding'] = encoding

	with open(path_dataset , "wb") as f:
		pickle.dump(data,f)

	return True

