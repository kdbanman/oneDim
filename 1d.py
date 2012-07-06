# render subset of environment.  view moved by mouse position, user-selectable width
# if positive state an negative state try and occupy the same cell; it dies, all live/dead cells in direct contact die, or just surrounding cells die?

import pygame, sys
from pygame.locals import *

import random

def render(env, gen, len):

	x = 0
	top = (gen*3)%(len)
	
	for cell in env:
		
		if cell == 1:
			color = liveColor
		else:
			color = whiteColor

		left = 3*x
		pygame.draw.rect(windowSurf,color, (left, top, 3, 3))

		x = x + 1

	pygame.display.update()

def iterate(env):

	newEnv = []	
	i = 0
	while i < len(env):

		local = (env[(i-1)%len(env)],env[i],env[(i+1)%len(env)])

		if local in liveSet:
			state = 1
		


		else:
			state = 0

		newEnv.append(state)	
		i = i + 1	
	
	
	return newEnv	


size = int(input('environment size: '))
lifespan = int(input('lifespan: '))
#until we have a controllable render subset, render width needs to be 3*size to be meaningful
window = int(input('render width: '))

antiState = input('antistate? (1 for yes, 0 for no) ')
if antiState == 1:
	antiState = True

renderMode = int(input('mode: '))
if renderMode == 3:
	prob = int(input('probability: '))

if renderMode == 4:
	width = size
	while width >= size or width <= 0:
		width = int(input('block width: '))

window = window - window%3 
length = 798

pygame.init()

windowSurf = pygame.display.set_mode((window,length))
pygame.display.set_caption('1D Automata, Bitch')
whiteColor = pygame.Color(255,255,255)
liveColor = pygame.Color(0,0,0)


liveSet = set( ((0,0,1),(1,1,0),(0,1,1),(0,1,0),(1,0,1)) )

environment = []

i = 0

if renderMode == 1:

	while i < size:
		if i == int(size/2):
			environment.append(1)
		else:
			environment.append(0)
		i = i + 1

if renderMode == 2:

	while i < size:
		if i >= int(2*size/5) and i <= int(3*size/5):
			environment.append(1)
		else:
			environment.append(0)
		i = i + 1

if renderMode == 3:

	while i < size:
		if random.randint(0,100) < prob:
			environment.append(1)
		else:
			environment.append(0)
		i = i + 1

if renderMode == 4:

	while i < size:
		if i%2 == 0 and i >= int((size - width)/2) and i <= int((size + width)/2):
			environment.append(1)
		else:
			environment.append(0)
		i = i + 1

if antiState:
	
	antiEnv = []

	i = 0
	while i < size:
		if i == 0:
			antiEnv.append(1)
		else:
			antiEnv.append(0)
		i = i + 1

generation= 0

while generation < lifespan:
	
	render(environment, generation, length)
	
	environment = iterate(environment)
	
	if antiState == True:
		antiEnv = iterate(antiEnv)
		i = 0
		while i < len(environment):
			if antiEnv[i] == 1 and environment[i] == 1:
				antiEnv[i] = 0
				environment [i] = 0
			i = i + 1
	generation = generation + 1

