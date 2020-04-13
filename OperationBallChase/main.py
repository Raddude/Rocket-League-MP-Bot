#Test
import cv2
import cv
import keyboard
import time
import numpy as np
import pyautogui
from PIL import Image
from mss import mss
from CarControl.StateManager import *


FRAME_RATE = 20
SLEEP_TIME = 1/FRAME_RATE
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
WINDOW_X = 0-WINDOW_WIDTH
WINDOW_Y = 50
count = 0
display_size = {'top' : WINDOW_Y, 'left' : WINDOW_X, 'width' : WINDOW_WIDTH, 'height' : WINDOW_HEIGHT}

programRunning = True

lower_boost_HSV_filter = np.array([23, 53, 152])
upper_boost_HSV_filter = np.array([42, 133, 255])

	

with mss() as sct:
	while(programRunning):
		for num, monitor in enumerate(sct.monitors[1:], 1):

			last_time = time.time()
			fps = 0

			while time.time() - last_time < 1:
				img = np.asarray(sct.grab(display_size))


				img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
				boost_filtered_image = cv2.inRange(img, lower_boost_HSV_filter, upper_boost_HSV_filter)


				cv2.imshow("Image Capture", boost_filtered_image)


				#Quit with the P key
				if cv2.waitKey(80) & 0xFF == ord("p"):
					programRunning = False

				fps += 1

			print(fps)

cv2.destroyAllWindows()