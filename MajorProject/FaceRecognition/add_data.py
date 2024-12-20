import face_recognition as fr
import pickle 
import cv2
from model import load_data

path = 'dataset.pkl'

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

	with open(path , "wb") as f:
		pickle.dump(data,f)

	return True

print(len(load_data()))

#get_data("Roger Federer", "C:/Users/hp/OneDrive/Desktop/Riz/opencv_facerecognition/dataset/Original Images/Original Images/Roger Federer/Roger Federer_2.jpg")

