import matplotlib.pyplot as plt
import numpy as np
import random
import math
ini_max_v = 0.5
probability_scatter = 0.05
class particle():
	def __init__(self):
		self.xpos = random.random()
		self.ypos = random.random()
		self.xv = np.random.randn()*ini_max_v**2
		self.yv = np.random.randn()*ini_max_v**2
class material():

	def __init__(self):
		self.array_electn = []
		for i in range(100):
			a = particle()
			self.array_electn.append(a)
	def electron_amount(self,t):
		return int(10*math.exp(-t))
	def electron_input(self,t):
		for i in range(self.electron_amount(t)):
			b = particle()
			b.xpos = 0
			b.ypos = random.random()
			b.xv = random.random()
			b.yv = random.random()*2 - 1
			self.array_electn.append(b)

	def scatter(self,delta_t):
		for i in range(len(self.array_electn[:])):
			#updating position
			self.array_electn[i].xpos += self.array_electn[i].xv*delta_t
			self.array_electn[i].ypos += self.array_electn[i].yv*delta_t
			##bouncing back
			if (self.array_electn[i].ypos > 1):
				delta_y = self.array_electn[i].ypos - 1
				self.array_electn[i].ypos =  1 - delta_y
				self.array_electn[i].yv = -self.array_electn[i].yv
			elif(self.array_electn[i].ypos < 0):
				self.array_electn[i].ypos = -self.array_electn[i].ypos
				self.array_electn[i].yv =   -self.array_electn[i].yv

		## pass through if x<0 or x>1
 		self.array_electn[:] = filter(lambda x: (x.xpos < 1) and (x.xpos > 0),self.array_electn[:])		
		##Update velocity
		length = int(len(self.array_electn[:])*probability_scatter)
		for i in range(length):
			random_index = random.randint(0,len(self.array_electn[:]) - 1)
			self.array_electn[random_index].xv = np.random.randn()*ini_max_v**2
			self.array_electn[random_index].yv = np.random.randn()*ini_max_v**2
	
delta_t = 0.5
mat = material()
t = 0
simulation_duration = 11
while (t <= simulation_duration):

	mat.electron_input(t)
	mat.scatter(delta_t)
	plt.figure()
	for i in range(len(mat.array_electn[:])):

		plt.plot([mat.array_electn[i].xpos, mat.array_electn[i].xpos + mat.array_electn[i].xv*delta_t],[mat.array_electn[i].ypos,mat.array_electn[i].ypos+mat.array_electn[i].yv*delta_t],c = 'b', ls = '-')
		
		plt.plot(mat.array_electn[i].xpos,mat.array_electn[i].ypos,'ro')

	t += delta_t
plt.show()

