import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('twstock.sqlite3')

df = pd.read_sql("Select * from s2330", conn)
df = df.sort_values('日期')
plt.figure( figsize=(10,5), dpi=50)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.xticks(range(0,100,10),rotation=45)
plt.plot(df['日期'][750:],df['收盤價'][750:],label='收盤價')
plt.plot(df['日期'][750:],df['最高價'][750:],label='最高價')
plt.plot(df['日期'][750:],df['最低價'][750:],label='最低價')
plt.legend()
plt.grid()
plt.savefig('chart.png')
plt.show()
#print(df)
#['107/01/20','108/01/20','109/01/20','110/01/20']
