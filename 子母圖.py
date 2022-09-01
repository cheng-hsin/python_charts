import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
a1 = fig.add_axes([0.01,0.1,3, 2])
a2 = fig.add_axes([2.1,0.2,0.8,0.3])
x = [1,3,5,7,9]
y1=[6,3,1,8,4]
y2=[9,7,5,3,6]
a1.plot(x,y1)
a2.plot(x,y2)
plt.show()