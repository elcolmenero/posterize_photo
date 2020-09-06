
from PIL import Image
import numpy as np
import pygame
import cv2


# Name of image in the same folder of this Python File
filename = "example_photo.jpg"

# Posterize Grade. 3 is MIN, 250 os MAX
 # 3 -> 20 is the better RANGE
sensitive = 50

# New Generated File Name
name = "posterize.jpg"



def main():
	global filename

	# IMAGE STUFF
	
	image = Image.open( filename )
	size = width, height = image.size

	#GENERATE POST IMG
	imgMatrix = np.zeros((width, height , 3), dtype=np.uint8)
	imgMatrix = iterateImage(width, height, image, 0, imgMatrix, 0)


	i=Image.fromarray(imgMatrix,"RGB")
	i.show()
	i.save(name) 

	del image;

def iterateImage(width, height, image, screen, imgMatrix, index):

	totalLoop = width *height
	percentaje = 0
	roundper = 0
	last = 0
	currentLoop = 0

	for xpixel in range(width):
		for ypixel in range(height):	
			coordinate = xpixel, ypixel

			cColor = red, green, blue = image.getpixel( coordinate )		#Get INT Pixel Color
			currentHEX = roundRGB(red, green, blue, index)			#Round RGB and turn to HEX
			
			imgMatrix[xpixel, ypixel] = currentHEX

			currentLoop+=1
			if xpixel != 0 and ypixel != 0:
				percentaje = ((currentLoop/totalLoop)*100)
				roundper = round(percentaje)

			if roundper != last:
				print(roundper, "%")
				last = roundper
			


	return imgMatrix


def roundRGB(red, green, blue, index):
	global sensitive

	loopCount = 250/sensitive

	for index in range(int(sensitive)):
		if red < loopCount*index:
			red = loopCount*index
			break
	for index in range(int(sensitive)):
		if blue < loopCount*index:
			blue = loopCount*index
			break
	for index in range(int(sensitive)):
		if green < loopCount*index:
			green = loopCount*index
			break

	red = 250 if red > 250 else red
	green = 250 if green > 250 else green
	blue = 250 if blue > 250 else blue

	red = 0 if red < 0 else red
	green = 0 if green < 0 else green
	blue = 0 if blue < 0 else blue


	rgbColor = (red, green, blue)

	return rgbColor

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

if __name__ == "__main__":
	main()