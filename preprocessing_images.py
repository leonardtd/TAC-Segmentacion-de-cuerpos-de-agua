import numpy
import cv2
import os
import shutil

size = 128


def load_images_from_folder(folder, isInput_img=True):
	images = []
	filenames = []
	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_COLOR)
		if img is not None:
			img = cv2.resize(img, (size, size))
			if isInput_img:
				H, S, V = cv2.split(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
				eq_V = cv2.equalizeHist(V)
				img = cv2.cvtColor(cv2.merge([H,S,eq_V]),cv2.COLOR_HSV2BGR)
			else: #mask image
				img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			images.append(img)
			filenames.append(filename)

	return numpy.array(images), filenames

def move_files(images, filenames, dest):
	for image, filename in zip(images, filenames):
		cv2.imwrite(os.path.join(dest , filename), image)

images, fileImages = load_images_from_folder('./Water Bodies Dataset/Images')
masks, fileMasks = load_images_from_folder('./Water Bodies Dataset/Masks',False)

			
move_files(images, fileImages,'./Water Bodies Dataset/Resized Images')
move_files(masks, fileMasks,'./Water Bodies Dataset/Resized Masks')
