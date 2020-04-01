#Single Key Actions
#
#This file controls every base action possible with default controls in Rocket League

import keyboard
import mouse
import time

driveForward = False
driveBackward = False
turnLeft = False
turnRight = False
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
	driveForward = state
	return driveForward

def setBackward(state):
	driveBackward = state
	return driveBackward

def turnLeft(state):
	turnLeft = state
	return turnLeft

def turnRight(state):
	turnRight = state
	return turnRight

def jump(state):
	jumping = state
	return jumping

def boost(state):
	boosting = state
	return boosting

def powerslide(state):
	sliding = state


	


def runCar():

	if driveForward:
		keyboard.press('w')
	else:
		keyboard.release('w')


	if driveBackward:
		keyboard.press('s')
	else:
		keyboard.release('s')

		
	if turnLeft:
		keyboard.press('l')
	else:
		keyboard.release('l')


	if turnRight:
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


	if powerslide:
		keyboard.press('shift')
	else:
		keyboard.release('shift')