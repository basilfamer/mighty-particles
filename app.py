import pygame
import random

#Create window
window = pygame.display.set_mode((400,300))
pygame.display.set_caption("Particle")

#Array used to hold all Particle instances
particles = []

#################
#### METHODS ####
#################

#Add's a particle to the center of the screen
def add_particle():
	p = Particle(200,150,10)
	particles.append(p)

#################
#### CLASSES ####
#################

class Particle:

	#Initialization
	def __init__(self,x,y,size):

		#Set local variables
		self.x = x
		self.y = y
		self.size = size
		self.color = (random.random()*255,random.random()*255,random.random()*255)
		self.yspeed = int(-5+(random.random())*10-random.random()*5)
		self.xspeed = int(-5+(random.random())*10)

		#We don't let particles have an xspeed of 0
		while self.xspeed == 0:
			self.xspeed = int(-3+(random.random())*6)

	#Draw method
	def display(self):
		if self.y > 300 + self.size:
			return
		self.y += self.yspeed
		self.x += self.xspeed
		if tick % 4 == 0:
			self.yspeed += 1
		self.size += 5
		pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

##################
##### LOGIC  #####
##################

#Used to keep constant time
clock = pygame.time.Clock()

#Used to represent current time
tick = 0

#Main Loop
Running = True
while Running:
	#Quit game if quit event is passed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Running = False

	#Every 10 ticks
	#Add a particle
	if tick % 5 == 0:
		add_particle()
		add_particle()
		add_particle()
		add_particle()

	#Clear screen
	window.fill((0,0,0))

	#DRAWING CODE

	#Draw each particle
	for p in particles:
		p.display()

	#Update display
	pygame.display.flip()

	#Clock stuff
	clock.tick(60)
	tick+=1
