

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10,21)
y1=x**3 - 5*x**2 + 15*x - 29
y2=-2*x**3 + 11*x**2 - 16*x + 18
print(x)
print(y1)
print(y2)
plt.xlim(-5,10)
plt.ylim(-1000,1000)
plt.xlabel('老度')
plt. ylabel('薪水')
plt.xticks([-4, 0, 8], ['年輕' , '中年', '老'])
plt.yticks([-1000,-280, 310,750], ['差', '一般', '棒', '超棒'])
# plt.grid()
plt.title("什麼鬼的圖",fontsize=20)
plt.plot(x,y1,label="男生")
# plt.plot(x, y2, color=(0, 0.5, .7))
plt.plot(x, y2, "r-.o",label="女生")
plt.rcParams['font.sans-serif']="DFKai-SB"
# plt.plot(x, y2, color='m')
plt.show()