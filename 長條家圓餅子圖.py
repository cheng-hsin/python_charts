import matplotlib.pyplot as plt
import numpy as np

rating = [20,30,40,10]
labels = ["Jun", "Jul", "Aug", "Sep"]
index = np.arange(len(labels))

plt.figure()
plt.subplot(1,2,1)
plt.bar(index,rating,color='b')
plt.xticks(index,labels)



plt.subplot(1,2,2)
plt.axis("equal")
exp = [0, 0, 0.1, 0]
plt.pie( rating, explode=exp, labels=labels, labeldistance=1.1, autopct='%2.1f%%', pctdistance=0.6)
plt.show()



plt.savefig("chart.png")
plt.colse()


