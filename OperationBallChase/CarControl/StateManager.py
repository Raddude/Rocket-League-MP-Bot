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

def setBackward(state):
	driveBackward = state

def turnLeft(state):
	turnLeft = state

def turnRight(state):
	turnRight = state

def jump(state):
	jumping = state

def boost(state):
	boosting = state

def powerslide(state):
	sliding = state
	