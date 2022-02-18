import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci

def instant_plot(xL0,xR0,xL,xR):
    xmin=xL0
    xmax=xR0
    
    x=np.linspace(xmin,xmax,100)
    y=g(x)
    plt.plot(x,y,color='black')
    plt.axvline(x=xL,color='red')
    plt.axvline(x=xR,color='blue')
    plt.axhline(y=0,color='pink')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
def g(x):
    return sci.erf(x)-0.5
xL0=0
xR0=2
tolerance=10**(-6)
xL=xL0
xR=xR0
instant_plot(xL0,xR0,xL,xR)
g(xL)*g(xR)<0
if(g(xL)*g(xR)<=0):
    xn=(xL+xR)/2
    if(g(xL)*g(xn)<=0):
        xR=xn
    else: 
        xL=xn
        
    while (np.fabs(xL-xR)>=tolerance):
        instant_plot(xL0,xR0,xL,xR)
        xn=(xL+xR)/2
        if(g(xL)*g(xn)<=0):
            xR=xn
        else:
            xL=xn
    xr=xL
    print(xr)
else:
    print("try other xL and xR")                


