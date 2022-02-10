import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
fontname={'fontname':'Times New Roman'}
cm=1/2.54

x=np.linspace(-1,1,50)
y=np.linspace(-1,1,50)
X,Y=np.meshgrid(x,y)
f=(Y)
extent=[min(x),max(x),min(y),max(y)]


fig = plt.figure(dpi=300)
fig,ax = plt.subplots(figsize=(9*cm,6*cm))
im=plt.pcolormesh(X,Y,f,shading='auto',cmap=plt.cm.RdBu)
ax.set_aspect('equal','box')
ax.set(xlim=(-1,1),ylim=(-1.05,1.05))
plt.xticks(np.arange(-1,1+0.1,0.25),fontsize=8,**fontname)
plt.yticks(np.arange(0,1+0.1,0.25),fontsize=10,**fontname)
colorbar=plt.colorbar(im)
colorbar.set_label('colorbar',rotation=270,fontsize=8)
plt.title(r'$f=y$')
cset=plt.contour(X,Y,f,np.arange(-1,1+0.1,0.2),colors='black')
plt.clabel(cset,inline=True, fontsize=8)



plt.show()
fig.savefig('aaa.eps',format='eps',bbox_inches='tight',dpi=300)