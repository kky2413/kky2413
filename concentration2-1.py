import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
fontname={'fontname':'Times New Roman'}
cm=1/2.54
xmin=0
xmax=10
resolution=1000
d=10000
t=0.0001
x=np.linspace(xmin, xmax,resolution)
y=x*(4*d*t)**(1/2)



fig = plt.figure(dpi=300)
fig,ax = plt.subplots(figsize=(9*cm,6*cm))
ax.plot(x,y,color='red', marker='*',markevery=2, linestyle='solid', linewidth=0.5, markersize=1)
plt.xlabel("x",fontsize=10)
plt.ylabel("y",fontsize=10)
plt.xticks(np.arange(0.25,0.251 ,0.1),fontsize=10,**fontname)
plt.yticks(np.arange(0.49,0.51,0.02),fontsize=10,**fontname)
plt.xlim([0.2,0.3])
plt.ylim([0.5,0.6])
plt.legend([r'$c1=1-erf(\frac{x}{\sqrt{4dt}}) $',r'$c2=1-erf(\frac{x}{\sqrt{4dt2}}) $',r'$c3=1-erf(\frac{x}{\sqrt{4dt3}}) $',
            r'$c4=1-erf(\frac{x}{\sqrt{4dt4}}) $'],
           loc='upper left',fontsize=6,ncol=2)

plt.show()
fig.savefig('ccc22.png',format='png',bbox_inches='tight',dpi=300)