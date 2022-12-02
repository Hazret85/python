import cv2
import pytesseract
# import numpy as np
# from tensorflow import keras
# from keras.datasets import mnist
# from keras.layers import Dense, Flatten

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = x_train / 255
# x_test = x_test / 255
#
# y_train_cat = keras.utils.to_categorical(y_train,10)
# y_test_cat = keras.utils.to_categorical(y_test,10)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# cv2.imshow('res',gray)
# cv2.waitKey()


for iterate in range(0,9):
	image_file = "images/{}.jpeg".format(iterate)
	img = cv2.imread(image_file)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, threshold_image = cv2.threshold(img, 180, 255, 0)
	with open('text{}.txt'.format(iterate),'w',encoding='utf-8') as file:
		if len(pytesseract.image_to_string(threshold_image,lang='rus')) > 20:
			file.write(pytesseract.image_to_string(threshold_image,lang='rus'))
		else:
			file.write(pytesseract.image_to_string(img,lang='rus'))




