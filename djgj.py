from matplotlib import pyplot as plt
import numpy as np
s='single_crystal_test_out.csv'
data=np.genfromtxt(s,delimiter=",",names=True)


plt.plot(data['e_zz'],data['stress_zz'],linewidth=3, c='#FF9999',marker='*',markersize=16,linestyle='--')
plt.xlabel(r'$\epsilon_{zz}$',fontsize=10,color='red') # r'$수식$' 형식을 이용해서 epsilon_zz를 그리스문자 epsilon 및 아래첨자 zz로 변환
plt.ylabel(r'$\sigma_{zz}$',fontsize=10,color='red')  # r'$수식$' 형식을 이용해서 sigma_zz를 그리스문자 sigma 및 아래첨자 zz로 변환
  #더 많은 정보: https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html
plt.title('single crystal test',fontsize=20,color='#66BEFF')
plt.tick_params(axis='x', labelsize=11,labelcolor='#FF66B2',color='red')
plt.tick_params(axis='y', labelsize=13,labelcolor='#FF66B2',color='red')

plt.show()


