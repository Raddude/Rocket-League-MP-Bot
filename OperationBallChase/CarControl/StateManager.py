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



def setForward(state):
	drivingForward = state
	return driveForward

def setBackward(state):
	drivingBackward = state
	return driveBackward

def turnLeft(state):
	turningLeft = state
	return turnLeft

def turnRight(state):
	turningRight = state
	return turnRight

def jump(state):
	jumping = state
	return jumping

def boost(state):
	boosting = state
	return boosting

def powerslide(state):
	sliding = state
	return sliding


	


def runCar():

	#Multiple key actions
	# if __ and ___




	#Single actions
	if drivingForward:
		keyboard.press('w')
	else:
		keyboard.release('w')


	if drivingBackward:
		keyboard.press('s')
	else:
		keyboard.release('s')

		
	if turningLeft:
		keyboard.press('l')
	else:
		keyboard.release('l')


	if turningRight:
		keyboard.press('r')
	else:
		keyboard.release('r')


	if jumping:
		mouse.press('right')
	else:
		mouse.release('right')


	if boosting:
		mouse.press('left')
	else:
		mouse.release('left')


	if sliding:
		keyboard.press('shift')
	else:
		keyboard.release('shift')