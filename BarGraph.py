import numpy as np
import matplotlib.pyplot as plt
n=10
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.figure()
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
for x,y in zip(X,Y1):
    plt.text(x,y+0.02,'%.2f'%y,ha='center',va='bottom')
for x,y in zip(X,Y2):
    plt.text(x,-y-0.15,'%.2f'%y,ha='center',va='bottom')
    plt.ylim(-1.1,1.1)