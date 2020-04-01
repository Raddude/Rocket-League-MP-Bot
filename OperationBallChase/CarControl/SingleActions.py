#Single Key Actions
#
#This file controls every base action possible with default controls in Rocket League

import keyboard
import mouse
import time



def pressKeyForTime(key, runTime):
	keyboard.press(key)
	time.sleep(runTime)
	keyboard.release(key)

def pressMouseForTime(key, runTime):
	mouse.press(button=key)
	time.sleep(runTime)
	mouse.release(button=key)



def driveForward(runTime):
	pressKeyForTime('w', runTime)

def driveBackward(runTime):
	pressKeyForTime('s', runTime)

def steerLeft(runTime):
	pressKeyForTime('a', runTime)

def steerRight(runTime):
	pressKeyForTime('d', runTime)

def jump(runTime):
	pressMouseForTime('right', runTime)

def boost(runTime):
	pressMouseForTime('left', runTime)

def powerslide(runTime):
	pressKeyForTime('shift', runTime)
	