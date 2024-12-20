import pickle
import cv2
import face_recognition as fr
import path
import sys


dir = path.Path(__file__).abspath()
sys.append.path(dir.parent.parent)

path_dataset = 'dataset.pkl'

#Unpickle dataset
def load_data():
	with open(path_dataset, 'rb') as f:
		data = pickle.load(f)
	return data 


#Face Recognition function based on face_recognition library
def recognize(image, tolerance):

	data = load_data()

	#128-dimensional face encoding for each face. Storing known face encodings in list known_faces.
	known_faces = [data[i]["encoding"] for i in data.keys()]
	#Storing names of all the known people in the known_names list.
	known_names = [data[i]["name"] for i in data.keys()]

	#image = fr.load_image_file(image)

	#Finding coordinates of faces in the image
	locations = fr.face_locations(image)
	#Encoding located faces
	encodings = fr.face_encodings(image, locations)

	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	#Matching faces in unknown image to that of known images

	for face_encodings, face_locations in zip(encodings,locations):
		top,right,bottom,left = face_locations
		color = [0,255,0]

		#Calculating Euclidean distance between known and unknown faces
		results = fr.compare_faces(known_faces, face_encodings, tolerance)

		match = None
		name = "Unknown"

		if True in results:
			idx = results.index(True)

			name = known_names[idx]

			top,right,bottom,left = face_locations
			color = [128,255,0]

		cv2.rectangle(image, (left,top), (right,bottom), color, 3)

		cv2.putText(image, name, (left, top-10),cv2.FONT_HERSHEY_DUPLEX,0.75,(127,0,255),2)

	return image,name

