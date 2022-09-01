import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-101, 101, 10)
y1= x**3-5*x**2+15*x-29
y2=-2*x**3+11*x**2-16*x+18
print(x)
print(y1)
plt.xlim(-100,100)
plt.plot(x,y1)
plt.plot(x, y2, color=(0, 0.5, 0.7))
plt.plot(x,y2, "r-.o")
# plt.plot(x, y2, color='m')
plt.show()