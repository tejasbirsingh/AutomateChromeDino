import pyautogui
from PIL import Image , ImageGrab

import time

def hit(key):
	pyautogui.keyDown(key)
	return

def isCollide(data):
	for i in range(250,300):
		for j in range(410,548):
			if data[i,j] >  100:
				hit("down")
				time.sleep(1)
				pyautogui.keyUp("down")
				return 			

	for i in range(275,505):
		for j in range(548,650):
			if data[i,j]  > 100:
				hit("up")
				return 
				

	return 


def takeScreenshot():
	image = ImageGrab.grab().convert('L')
	
	return image


if __name__ == "__main__":
	time.sleep(3)
	hit('up')
	while True:
		image = takeScreenshot()
		data = image.load()
		isCollide(data)
		
		# for i in range(250,300):
		# 	for j in range(410,548):
		# 		data[i,j]  = 220
		
		# # for cactus		
		# for i in range(275,510):
		# 	for j in range(548,650):
		# 		data[i,j] =  170
				
		# image.show()
		# break
		# 