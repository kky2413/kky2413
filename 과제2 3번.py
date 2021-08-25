from random import random

fout=open('random.txt','w')
for a in range(200):
    rand_num = random()*150 - 50
    print(rand_num,file=fout)

fout.close()




