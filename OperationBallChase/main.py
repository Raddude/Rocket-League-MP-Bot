#Test
import cv2
import keyboard
import time
from CarControl.StateManager import *

programRunning = True
framerate = 20
sleep_time = 1/framerate
count = 0

	
	
while(programRunning):

	runCar()
	print(count/framerate)

	time.sleep(sleep_time)

	if keyboard.is_pressed('p'):
		programRunning = False

	count = count + 1