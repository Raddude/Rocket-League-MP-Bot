#Test
import cv2
import keyboard
import time
from CarControl.StateManager import *

framerate = 20
sleep_time = 1/framerate



while(True):

	runCar()

	time.sleep(sleep_time)