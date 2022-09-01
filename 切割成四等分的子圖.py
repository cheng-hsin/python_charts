import matplotlib.pyplot as plt
import numpy as np
np1 = np.array([[14,16,8,13,16,12,16,5],
[10,19,6,10,13,13,20,9]])
lb1=['創業理財','文學小說','藝術設計','人文科普','語言電腦','心靈養生','生活風格','親子共享']
plt.figure()
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'


plt.subplot(2,2,1)
plt.title('圖書分類銷售比率-男性')
plt.pie(np1[0], labels=lb1, autopct='%2.1f%%')

plt.subplot(2,2,2)
plt.title('圖書分類銷售比率-女性')
plt.pie(np1[1], labels=lb1, autopct='%2.1f%%')

plt.subplot(223)
plt.bar(np.arange(1,len(lb1)+1)-0.2,
np1[0],width=0.4,label='男')
plt.bar(np.arange(1,len(lb1)+1)+0.2,
np1[1], width=0.4, label='女')
plt.xlabel('圖書分類')
plt.ylabel('銷售比率(%)')
plt.title('圖書分類銷售長條圖-性別')
plt.xticks(range(1,9), lb1, rotation=45)
plt.yticks(np.arange(0,20.5,2.5))
plt. legend()

plt.subplot(224)
plt.plot(lb1, np1[0], marker='s',
label='男')
plt.plot(lb1, np1[1], marker='s',
label='女')
plt.legend()
plt.xticks(rotation=45)
plt.yticks(range(6,21,2))
plt.xlabel('圖書分類')
plt.ylabel('銷售比率(%)')
plt.title('圖書分類銷售折線圖-性別')
plt.grid()
plt.show()