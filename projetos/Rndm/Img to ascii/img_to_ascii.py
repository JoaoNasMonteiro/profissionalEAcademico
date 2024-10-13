import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

#Takes in input image
ImagePathInput = str(input("Enter a valid file path:"))
InputImage = cv.imread(ImagePathInput)

if os.path.exists(ImagePathInput):

	#resizes image
	Resized = cv.resize(InputImage, (0,0), fx = 0.2, fy = 0.2)

	#grayscales the resized image
	GrayImage = cv.cvtColor(Resized, cv.COLOR_BGR2GRAY)
	GrayShape = GrayImage.shape

	#creates a new image array
	OutputImage = [] 


	# grabs correct ascii value for the new gray pixel and appends it to the output image
	i = 0
	for row in GrayImage:
		for GrayPx in row:
			if GrayPx == 0: 
				OutputImage.append(" ")
			elif 0 < GrayPx <= 50:
				OutputImage.append(".")
			elif 50 < GrayPx <= 100:
				OutputImage.append(":")
			elif 100 < GrayPx <= 150:
				OutputImage.append("*")
			elif 150 < GrayPx <= 200:
				OutputImage.append("%")
			elif 200 < GrayPx <= 255:
				OutputImage.append("#")

			i = i+1

			if i % GrayShape[1] == 0:
				OutputImage.append("\n")

	# writes to the output file
	with open('output.txt', 'w') as file:
		for Px in OutputImage:
			file.write(Px)

	print("Written successfully to the output file output.txt")
	exit()


		

else:
	print("Image file could not be accessed. Try again with a valid file path")
	exit()


