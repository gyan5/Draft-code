import matplotlib.pyplot as plt
import numpy as np
import random
import math

ini_max_v = 0.5
initial_C 
electn_ipt
delta_t
def initial_condition():
	x  =[]
	y  =[]
	vx =[]
	vy =[]
	#fig=plt.figure()
#	ax =fig.add_subplot(111,aspect="equal")
	for i in range(100):
		a = random.random()
		b = random.random()
		x.append(a)
		y.append(b)
		va=np.random.randn()*ini_max_v**2
		vb=np.random.randn()*ini_max_v**2
		vx.append(va)
		vy.append(vb)
		plt.plot(x,y,'ro')
		plt.plot([a,a+va],[b,b+vb],'-')
	plt.show()
	return [x,y,vx,vy]
def electron_amount(t):
	return int(100*math.exp(-t))
def electron_input(t):
	for i in range(electron_amount(t)):
		e_p_y = []
		Vx_electron =[]
		Vy_electron =[]
		a = random.random()
		e_p_y.append(a)
		vx = random.random()
		vy = random.random()*2 -1
	 	Vx_electron.append(vx)
		Vy_electron.append(vy)
	e_p_x = np.zeros(len(e_p_y))
	return [e_p_x,e_p_y,Vx_electron,Vy_elecrton]
def scatter(initial_C,delta_t):
	for i in range(len(initial_C[0][:])):
		initial_C[0][i] = initial_C[0][i]+initial_C[2][i]*delta_t
		initial_C[1][i] = initial_C[1][i]+initial_C[3][i]*delta_t
		

		
		
initial_C = initial_condition
electn_ipt = electron_input(time)
initial_C[0][:].extend(electn_ipt[0][:])
initial_C[1][:].extend(electn_ipt[1][:])
initial_C[2][:].extend(electn_ipt[2][:])
initial_C[3][:].extend(electn_ipt[3][:])
