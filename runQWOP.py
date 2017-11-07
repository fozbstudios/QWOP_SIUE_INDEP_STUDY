#!/usr/bin/python

import sys
import cv2
sys.path.append("webfiles/QWOP.js")
from QWOPcontrol import *
import numpy as np

#preprocess raw image to 80*80 gray image (FREAKING COMPUTER VISION HERE NBD)
def preprocess(observation):
	observation = cv2.cvtColor(cv2.resize(observation, (84, 110)), cv2.COLOR_BGR2GRAY)
	observation = observation[26: 110, :]
	ret, observation = cv2.threshold(observation, 1, 255, cv2.THRESH_BINARY)
	
	return np.reshape(observation, (84, 84, 1))
	
def playQWOP():
	#1: Init qwopAI
	#2: Init QWOP itself
	
	qwopInst = THIS WILL ATTACH TO OUR QWOP INSTANCE
	actions = DEFINE SOME ACTIONS HERE ZACH
	ai = qwopAI(actions)
	
	#3: play qwop
	#3.1 get initial state
	action0 = np.array([1,0,0,1]) #do nothing
	observation0, reward0, terminal = DO SOMETHING HERE
	observation0, cv2.cvtColor(cv2.resize(observation0, (84, 110)), cv2.COLOR_BGR2GRAY)
	observation0 = observation0[26:110, :]
	ret, observation0 = cv2.threshold(observation0, 1, 255, cv2.THRESH.BINARY)
	ai.setInitState(observation0)
	
	#3.2 run game
	while 1 != 0:
		action = ai.getAction()
		nextObservation, reward, terminal = DO SOMETHING HERE
		nextObservation = preprocess(nextObservation)
		ai.setPerception(nextObservation, action, reward, terminal)
		
def main():
	playQWOP()
	
if __name__ == '__main__':
	main()