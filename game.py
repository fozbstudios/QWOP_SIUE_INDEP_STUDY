#!/usr/bin/python

import numpy as np
import cv2
from random import randrange
from webfiles/

MAX_FRAMES_PER_EPISODE = 1000000
GAME_NAME = "QWOP AI"

class QWOP:
	def __init__(self):
		self.max_frames_per_episode = MAX_FRAMES_PER_EPISODE
		self.frame_skip = 4
		self.screen_width, self.screen_height = self.getScreenDimensions()
		self.legal_actions = [] #Need to put all of socket calls here
		self.action_map = dict()
		for i in range(leng(self.legal_actions)):
			self.action_map[self.legal_actions[i]] = i
			
		print len(self.legal_actions) #just to make sure that all 8 actions are there
		
		self.windowname = GAME_NAME
		cv2.startWindowThread()
		cv2.namedWindow(GAME_NAME)
		
	def get_image(self):
		numpy_surface = np.zeros(self.screen_height*self.screen_width*3, dtype=np.uint8)
		self.getScreenRGB(numpy_surface)
		image = np.reshape(numpy_surface, (self.screen_height, self.screen_width, 3))
		return image	
		
	def newGame(self):
		self.resetGame()
		return self.get_image()
		
	def next(self, action):
		reward = self.
	
	
		
	def getScreenDimensions():
		return width, height	
	
	def getScreenRGB(screen):
		
		
	def resetGame():
