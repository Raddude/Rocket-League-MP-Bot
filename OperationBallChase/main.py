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
targetingRunning = False
last_time = time.time()

lower_boost_HSV_filter = np.array([23, 53, 152])
upper_boost_HSV_filter = np.array([42, 133, 255])

lower_player_RGB_filter = np.array([240, 240, 240])
upper_player_RGB_filter = np.array([255, 255, 255])

H_filter_half_range = 10
S_filter_half_range = 30
V_filter_half_range = 40

scoreboard_height = 50
min_contour_area_for_nameplate = 100
max_contour_area_for_nameplate = 500
max_nameplate_height = 30
min_nameplate_width = 20
foundNameplate = False
acceptable_target_pillar_width = 5



	

with mss() as sct:
	while(programRunning):
		for num, monitor in enumerate(sct.monitors[1:], 1):

			#CAR CONTROL CODE

			#WASD CONTROL
			if keyboard.is_pressed('w') == True:
				setForward(state=True)
			else:
				setForward(state=False)

			if keyboard.is_pressed('s') == True:
				setBackward(state=True)
			else:
				setBackward(state=False)

			if keyboard.is_pressed('a') == True:
				turnLeft(state=True)
			else:
				turnLeft(state=False)

			if keyboard.is_pressed('d') == True:
				turnRight(state=True)
			else:
				turnRight(state=False)

			setBoost(state=False)



			#PROGRAM CONTROL
			if keyboard.is_pressed('i') == True:
				targetingRunning = True
			else:
				targetingRunning = False

			if keyboard.is_pressed('p') == True:
				programRunning = False

			runCar()










			#VISION CODE
			img = np.asarray(sct.grab(display_size))
			


			if targetingRunning == True:

				img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

				opponent_team_color_H = img[5, 450, 0]
				opponent_team_color_S = img[5, 450, 1]
				opponent_team_color_V = img[5, 450, 2]


				lower_boost_HSV_filter = np.array([opponent_team_color_H - H_filter_half_range, opponent_team_color_S - S_filter_half_range, opponent_team_color_V - V_filter_half_range])
				upper_boost_HSV_filter = np.array([opponent_team_color_H + H_filter_half_range, opponent_team_color_S + S_filter_half_range, opponent_team_color_V + V_filter_half_range])


				opponent_filtered_image = cv2.inRange(img, lower_boost_HSV_filter, upper_boost_HSV_filter)




				#Filter out scoreboard
				for x in range(WINDOW_WIDTH):
					for y in range(scoreboard_height):
						opponent_filtered_image[y, x] = 0



				#Find contours
				contours, heirarchy = cv2.findContours(opponent_filtered_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
				contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]


				#Filter contours
				nameplate_contour = 0

				for c in contours:
					this_contour_area = cv2.contourArea(c)

					enemy_br_x, enemy_br_y, enemy_br_w, enemy_br_h = cv2.boundingRect(c)
					nameplate_contour = c

					if this_contour_area > min_contour_area_for_nameplate and this_contour_area < max_contour_area_for_nameplate and enemy_br_h < max_nameplate_height and enemy_br_w > min_nameplate_width:
						foundNameplate = True
						break 

					foundNameplate = False



				#Display currently tracked name
				img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

				if foundNameplate:
					cv2.drawContours(img, [nameplate_contour], 0, (0, 255, 0), 2)



					#TRACKING CODE

					#Find position of enemy
					enemy_br_x, enemy_br_y, enemy_br_w, enemy_br_h = cv2.boundingRect(nameplate_contour)
					enemy_horizontal_screen_pos = enemy_br_x + (enemy_br_w/2)


					#Act based on the enemy's position
					if enemy_horizontal_screen_pos < (WINDOW_WIDTH/2) - acceptable_target_pillar_width:
						turnLeft(state=True)
					elif enemy_horizontal_screen_pos > (WINDOW_WIDTH/2) + acceptable_target_pillar_width:
						turnRight(state=True)
					setBoost(state=True)

				cv2.imshow("Image Capture", img)




			else:
				cv2.imshow("Image Capture", img)







			#Quit with the P key
			if cv2.waitKey(80) & 0xFF == ord("p"):
				programRunning = False



			fps = int(1/(time.time() - last_time))
			last_time = time.time()
			print(fps)

cv2.destroyAllWindows()