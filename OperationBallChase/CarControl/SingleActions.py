#Single Key Actions
#
#This file controls every base action possible with default controls in Rocket League

import keyboard
import time



def forward(runTime):
	keyboard.press('w')
	time.sleep(runTime)
	keyboard.release('w')