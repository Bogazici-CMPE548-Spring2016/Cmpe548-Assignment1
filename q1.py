import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getRandomR(dimension):
	u = np.random.rand(1)
	return np.power(u, 1.0/dimension)

def getRandomR3D():
	u = np.random.rand(1)
	return np.sqrt(u)

def getRandomTheta():
	u = np.random.rand(1)
	pi = np.pi
	return u * 2* pi

def getRandomThetaND(dimension):
	v = list()
	mean = np.zeros((dimension,), dtype=np.int)
	covariance = np.identity(dimension)
	v = np.random.multivariate_normal(mean,covariance,1).T
	return v

def getRandomCartesianPoint():
	r = getRandomR(2)
	theta = getRandomTheta()
	x = np.cos(theta) * r
	y = np.sin(theta) * r
	return x,y

N = 5000

#Question 1
for i in range(N):
	x,y = getRandomCartesianPoint()
	plt.plot(x,y,'bo')

plt.axis([-2,2,-2,2])
plt.show()


#BONUS
N = 5000
dimension = 3

if dimension==3:
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

v = list()
for i in range(N):
	r = getRandomR(dimension)
	v = getRandomThetaND(dimension)
	magnitude = 0
	for j in range(dimension):
		magnitude += np.power(np.abs(v[j]),2)

	magnitude = np.sqrt(magnitude)
	for j in range(dimension):
		v[j] = r * v[j] / magnitude
	
	if dimension == 3:
		ax.scatter(v[0], v[1], v[2], c='b', marker='o')

if dimension == 3:		
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.show()
