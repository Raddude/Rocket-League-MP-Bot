#State Manager
#
#This file controls a state manager for the buttons of the car

import keyboard
import mouse
import time

drivingForward = False
drivingBackward = False
turningLeft = False
turningRight = False
jumping = False
boosting = False
sliding = False




# def pressKeyForTime(key, runTime):
# 	keyboard.press(key)
# 	time.sleep(runTime)
# 	keyboard.release(key)

# def pressMouseForTime(key, runTime):
# 	mouse.press(button=key)
# 	time.sleep(runTime)
# 	mouse.release(button=key)



def setForward(state=False):
	global drivingForward
	drivingForward = state
	return drivingForward

def setBackward(state=False):
	global drivingBackward
	drivingBackward = state
	return drivingBackward

def turnLeft(state=False):
	global turningLeft
	turningLeft = state
	return turningLeft

def turnRight(state=False):
	global turningRight
	turningRight = state
	return turningRight

def setJump(state=False):
	global jumping
	jumping = state
	return jumping

def setBoost(state=False):
	global boosting
	boosting = state
	return boosting

def setPowerslide(state=False):
	global sliding
	sliding = state
	return sliding


	


def runCar():

	#Multiple key actions
	# if __ and ___




	#Single actions
	if drivingForward == True:
		keyboard.press('w')
	else:
		keyboard.release('w')


	if drivingBackward == True:
		keyboard.press('s')
	else:
		keyboard.release('s')

		
	if turningLeft == True:
		keyboard.press('l')
	else:
		keyboard.release('l')


	if turningRight == True:
		keyboard.press('r')
	else:
		keyboard.release('r')


	if jumping == True:
		mouse.press('right')
	else:
		mouse.release('right')


	if boosting == True:
		mouse.press('left')
	else:
		mouse.release('left')


	if sliding == True:
		keyboard.press('shift')
	else:
		keyboard.release('shift')