import matplotlib.pyplot as plt
import numpy as np
fontname={'fontname':'Times New Roman'}
xmin=0
xmax=1
resolution=100
x=np.linspace(xmin, xmax, resolution)
y=x*x
y2=np.sin(2*np.pi*x)
y3=np.cos(2*np.pi*x)
y4=x*np.log(x)+(1-x)*np.log(1-x)
y5=np.e**(-x**2)
y6=(1/2)+(1/2)*np.tanh((x-0.5)/0.01)

cm=1/2.54
fig = plt.figure(dpi=300)
fig,ax = plt.subplots(figsize=(9*cm,6*cm))
ax.plot(x,y,color='green', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,y2,color='red', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,y3,color='black', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,y4,color='blue', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,y5,color='orange', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,y6,color='pink', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=2)
plt.xlabel("x",fontsize=10)
plt.ylabel("y",fontsize=10)
plt.xticks(np.arange(0,1,0.1),fontsize=10,**fontname)
plt.yticks(np.arange(0,1,0.2),fontsize=10,**fontname)
plt.xlim([0.02,1])
plt.ylim([0.01,2])

plt.legend([r'$y=x^{2} $',r'$y2=sin(2\pi x) $',r'$y3=cos(2\pi x) $',
            r'$y4=x\log(x)+(1-x)\log(1-x) $',r'$y5=e^{-x^2} $',
            r'$y6=\frac{1}{2}+\frac{1}{2}tanh(\frac{x-0.5}{0.01}) $'],
           loc='upper left',fontsize=6,ncol=2)
plt.show()
fig.savefig('graph.png',format='png',bbox_inches='tight',dpi=300)

