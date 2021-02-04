import matplotlib.pyplot as plt
import numpy as np

def get_slp_intr(x,y):
	n=len(x)
	x_mean=sum(x)/n
	y_mean=sum(y)/n
	
	numer=0
	denom=0
	
	for i in range(n):
		numer+=(x[i]-x_mean)*(y[i]-y_mean)
		denom+=(x[i]-x_mean)**2
		
	slope = numer/denom
	intercept = y_mean - slope*x_mean
	return slope, intercept
	
x=[1,2,3]
y=[1.2,1.9,3.2]

m, c = get_slp_intr(x,y)

x = np.array(x)
y = np.array(y)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,'.')
plt.plot(x, m*x+c)

plt.show()
