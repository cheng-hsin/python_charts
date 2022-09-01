import numpy as np

np1 = np.genfromtxt('abc.txt', 'int64', delimiter=' ', encoding="utf-8",skip_header=1)

print('資料型態:{0}'.format(np1.dtype))
print('平均值：{0:.2f}'.format(np.mean(np1)))
print('中位數：{0:.2f}'.format(np.median(np1)))
print('標準差：{0:.2f}'.format(np.std(np1)))
print('變異數：{0:.2f}'.format(np.std(np1)**2))
print('極差值：{0:.2f}'.format(np.ptp(np1)))