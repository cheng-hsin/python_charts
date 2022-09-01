import matplotlib.pyplot as plt
import numpy as np

height = np.random.randint(140,185,15)
print(height)
weight = np.random.randint(40,110,15)
print(weight)
money = np.random.randint(300,1500,15)
print(money)
plt.grid()
plt.scatter(height,weight,s=money,alpha=0.5,marker='o',color='red')


height = np.random.randint(140,185,15)
print(height)
weight = np.random.randint(40,110,15)
print(weight)
money = np.random.randint(300,1500,15)
print(money)
plt.grid()
plt.scatter(height,weight,s=money,alpha=0.5,marker='o', color='blue')


plt.show