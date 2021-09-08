from matplotlib import pyplot as plt
import numpy as np
s='single_crystal_test_out.csv'
data=np.genfromtxt(s,delimiter=",",names=True)


plt.plot(data['e_zz'],data['stress_zz'],linewidth=3, c='#FF9999',marker='*',markersize=16,linestyle='--')
plt.xlabel('e_zz',fontsize=10,color='red')
plt.ylabel('stress_zz',fontsize=10,color='red')
plt.title('single crystal test',fontsize=20,color='#66BEFF')
plt.tick_params(axis='x', labelsize=11,labelcolor='#FF66B2',color='red')
plt.tick_params(axis='y', labelsize=13,labelcolor='#FF66B2',color='red')

plt.show()


