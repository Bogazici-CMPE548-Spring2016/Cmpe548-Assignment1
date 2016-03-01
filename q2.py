import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getRandomTheta():
	u = np.random.rand(1)
	pi = np.pi
	return u * 2* pi

def getRandomR():
	u = np.random.rand(1)
	return np.sqrt(u)

def getRandomCartesianPoint():
	r = getRandomR()
	theta = getRandomTheta()
	x = np.cos(theta) * r
	y = np.sin(theta) * r
	return x,y

def getRandomNumber(p, trial):
	x,y = getRandomCartesianPoint()
	check = np.power(np.fabs(x), p) + np.power(np.fabs(y), p)
	if check > 1:
		trial += 1
		plt.plot(x,y,'rx')
		return getRandomNumber(p, trial)
	else:
		return x,y,trial

def getRandomNumberSmarter(p, trial):
	u = np.sqrt(2)*(np.random.rand(1) - 0.5)
	v = np.sqrt(2)*(np.random.rand(1) - 0.5)
	angle = np.arctan(v/u) + np.pi / 4
	if u<0 and v<0:
		angle += np.pi
	elif v>0 and u<0:
		angle -= np.pi
	r = np.sqrt(np.power(u, 2) + np.power(v, 2))
	x = r * np.cos(angle)
	y = r * np.sin(angle)
	check = np.power(np.abs(x), p) + np.power(np.abs(y), p)
	if check > 1:
		trial += 1
		plt.plot(x,y,'rx')
		return getRandomNumberSmarter(p, trial)
	else:
		return x,y,trial

def rejectionSampling(p,N,square):
	trial = 0
	for i in range(N):
		if square==1:
			x,y,tr = getRandomNumber(p, 1)
		else:
			x,y,tr = getRandomNumberSmarter(p, 1)
		trial += tr
		plt.plot(x,y,'bo')
	return float(N) / trial

#used for the BONUS 2
def getRandomCoordinates(dimension, trial):
	ones = np.ones(dimension)
	v = np.random.rand(dimension) * 2 - ones
	zero = np.zeros(dimension)
	distance = np.linalg.norm(v-zero)
	if distance > 1:
		trial += 1
		if dimension == 3:
			ax.scatter(v[0], v[1], v[2], c='r', marker='x')
		return getRandomCoordinates(dimension, trial)
	else:
		return v, trial

#used for the BONUS 2
def rejectionSamplingBonus(dimension, N):
	trial = 0
	v = list()
	for i in range(N):
		v, tr = getRandomCoordinates(dimension, 1)
		trial += tr
		if dimension == 3:
			ax.scatter(v[0], v[1], v[2], c='b', marker='o')
	return float(N) / trial

plt.axis([-2,2,-2,2])
acceptanceRate = rejectionSampling(1.5, 5000, 1)
print "p=1.5, 1x1 square, acceptance rate = ", acceptanceRate
plt.show()

acceptanceRate = rejectionSampling(0.7, 5000, 1)
print "p=0.7, 1x1 square, acceptance rate = ", acceptanceRate
plt.show()

acceptanceRate = rejectionSampling(0.7, 5000, 0)
print "p=0.7, p=1 norm, acceptance rate = ", acceptanceRate
plt.show()

#BONUS 2
dimension = 3
if dimension==3:
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
acceptanceRate = rejectionSamplingBonus(dimension, 1000)
print "n-sphere, n-cube, acceptance rate = ", acceptanceRate
if dimension == 3:		
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.show()