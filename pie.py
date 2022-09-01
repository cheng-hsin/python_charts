import matplotlib.pyplot as plt
import numpy as np
n = [25, 40, 20, 15]
lbl = ["East", "West", "South", "North"]
clr = ["yellow", "green", "blue", "cyan"]
exp = [0, 0, 0.3, 0]
plt.pie( n, explode=exp, labels=lbl, colors=clr, labeldistance=1.1, autopct='%2.1f%%', pctdistance=0.5, shadow=True, startangle=0)
plt.show()