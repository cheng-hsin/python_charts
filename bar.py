import matplotlib.pyplot as plt
import numpy as np
x = np.array( [1,3,5,7,9] )
y1=[6,3,2,8,7]
y2 = [5,3,7,8,3]
plt.bar(x-0.41, y1, width=0.8)
plt.bar(x+0.41, y2, width=0.8)
plt.show()