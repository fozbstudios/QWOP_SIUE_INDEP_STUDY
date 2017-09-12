import matplotlib.pyplot as plt

from ipywidgets import widgets
from IPython.display import display

from matplotlib import animation
from JSAnimation.IPython_display import display_animation
from time import gmtime, strftime
import random
import cv2
import sys
from BrainDQN_Nature import *
import numpy as np

import gym

env = gym.make('SpaceInvaders-v0')
env.reset()
actions = env.action_space.n
brain = BrainDQN(actions)
