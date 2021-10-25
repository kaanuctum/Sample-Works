import os
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file))
image_dir = os.path.join(BASE_DIR,"images")
#depenends on where the cv2 modul is located on the computer
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')


recognizer = cv2.face.LBHFaceRecognizer_create()
#recognize could also use a deep learning library: tenserflow, pythorch, keras...

current_id = 0
label_ids  = {}
y_labels   = []
x_train    = []

for root, dirs, files is os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
			label = os.path.basename(root).replace(" ","_").lower()
			print(label,path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label_ids]
			print(label_ids)

#		 y_labels.append(label) #some number
#		 x_train.append(path)   #verify this image, turn it in to a numpy array in grayscale
		pil_immage = Image.open(path).convert("L")# greyscale
		image_array = np.array(pil_image,"uint8")
		print(image_array)
		faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5,minNeighbors=5)

		for (x,y,w,h) in faces:
			#roi: reagion of interest
			roi = image_array[y:y+h, x:x+w]
			x_train.append(roi)
			y_labels.append(id_)



with open("labels.pickle","wb") as f:
	pickle.dump(label_ids)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
