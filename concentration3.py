import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
fontname={'fontname':'Times New Roman'}
cm=1/2.54
tmin=0
tmax=100
resolution=10000
d=10000
t=np.linspace(tmin, tmax,resolution)
k=t**(1/2)
y=0.25*(4*d*t)**(1/2)



fig = plt.figure(dpi=300)
fig,ax = plt.subplots(figsize=(9*cm,6*cm))
ax.plot(k,y,color='red', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)

plt.klabel("k",fontsize=10)
plt.ylabel("y",fontsize=10)
plt.kticks(np.arange(1,10,1),fontsize=10,**fontname)
plt.yticks(np.arange(0,100,10),fontsize=10,**fontname)
plt.klim([0,10])
plt.ylim([0,100])

plt.legend([r'$c1=1-erf(\frac{x}{\sqrt{4dt}}) $',r'$c2=1-erf(\frac{x}{\sqrt{4dt2}}) $',r'$c3=1-erf(\frac{x}{\sqrt{4dt3}}) $',
            r'$c4=1-erf(\frac{x}{\sqrt{4dt4}}) $'],
           loc='upper left',fontsize=6,ncol=2)

plt.show()
fig.savefig('ccc33.png',format='png',bbox_inches='tight',dpi=300)