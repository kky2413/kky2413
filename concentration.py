import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
fontname={'fontname':'Times New Roman'}
cm=1/2.54
xmin=0
xmax=10
resolution=1000
d=10000
x=np.linspace(xmin, xmax,resolution)
t=0.00001
c=y=1-sci.erf(x/((4*d*t)**(1/2)))
t2=0.0002
c2=y2=1-sci.erf(x/((4*d*t2)**(1/2)))
t3=0.002
c3=y3=1-sci.erf(x/((4*d*t3)**(1/2)))
t4=0.02
c4=y4=1-sci.erf(x/((4*d*t4)**(1/2)))



fig = plt.figure(dpi=300)
fig,ax = plt.subplots(figsize=(9*cm,6*cm))
ax.plot(x,c,color='red', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,c2,color='blue', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,c3,color='orange', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)
ax.plot(x,c4,color='black', marker='*',markevery=2, linestyle='solid',
     linewidth=0.5, markersize=1)

plt.xlabel("x",fontsize=10)
plt.ylabel("y",fontsize=10)
plt.xticks(np.arange(1,10,1),fontsize=10,**fontname)
plt.yticks(np.arange(0,1,0.2),fontsize=10,**fontname)
plt.xlim([0,10])
plt.ylim([0,1])

plt.legend([r'$c1=1-erf(\frac{x}{\sqrt{4dt}}) $',r'$c2=1-erf(\frac{x}{\sqrt{4dt2}}) $',r'$c3=1-erf(\frac{x}{\sqrt{4dt3}}) $',
            r'$c4=1-erf(\frac{x}{\sqrt{4dt4}}) $'],
           loc='upper left',fontsize=6,ncol=2)

plt.show()
fig.savefig('ccc.png',format='png',bbox_inches='tight',dpi=300)