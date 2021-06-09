import numpy
import cv2
import os
import shutil

size = 128


def load_images_from_folder(folder, mapa=True):
	images = []
	filenames = []
	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder, filename))
		if img is not None:
			img = cv2.resize(img, (size, size))
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			if mapa:
				img = cv2.equalizeHist(img)
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
