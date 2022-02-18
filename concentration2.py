import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
fontname={'fontname':'Times New Roman'}
cm=1/2.54
tmin=0
tmax=10
resolution=1000
d=10000
t=np.linspace(tmin, tmax,resolution)
y=0.25*(4*d*t)**(1/2)



fig = plt.figure(dpi=300)
fig,ax = plt.subplots(figsize=(9*cm,6*cm))
ax.plot(t,y,color='red', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)

plt.tlabel("t",fontsize=10)
plt.ylabel("y",fontsize=10)
plt.tticks(np.arange(1,10,1),fontsize=10,**fontname)
plt.yticks(np.arange(0,1,0.2),fontsize=10,**fontname)
plt.tlim([0,10])
plt.ylim([0,1])

plt.legend([r'$c1=1-erf(\frac{x}{\sqrt{4dt}}) $',r'$c2=1-erf(\frac{x}{\sqrt{4dt2}}) $',r'$c3=1-erf(\frac{x}{\sqrt{4dt3}}) $',
            r'$c4=1-erf(\frac{x}{\sqrt{4dt4}}) $'],
           loc='upper left',fontsize=6,ncol=2)

plt.show()
fig.savefig('ccc22.png',format='png',bbox_inches='tight',dpi=300)