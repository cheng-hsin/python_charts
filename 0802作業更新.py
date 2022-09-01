import pandas as pd
import matplotlib.pyplot as plt

# 讀取檔案
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
df = pd.read_csv("TPMRT_P2.csv")

# 取出參數
xyear = df["年別"]
color=["tab:brown","tab:green","tab:red","tab:blue","tab:orange"]
pop=[df["BR"],df["G"],df["R"],df["BL"],df["O"]]
lbl=['文湖線','松山新店線','淡水信義線','板南線','中和新蘆線']

#ps.pie chart 每年
df1=df.set_index('年別')
plt.figure(figsize=(10,10),dpi=90) 
for i in range(0,5):
    plt.subplot(3,2,i+1)
    yy=df1.iloc[i]
    plt.pie(yy, labels=lbl ,colors=color,autopct='%2.2f%%')
    plt.title(str(df1.index[i])+'各線搭乘人次比例')
plt.show()

# 圓餅圖
popsum =[df["BR"].sum(),df["G"].sum(),df["R"].sum(),df["BL"].sum(),df["O"].sum()]
plt.figure(figsize=(7,5),dpi=90)
plt.title("臺北捷運104至108年總運量比例")
plt.pie(popsum,labels=lbl,colors=color,autopct="%2.2f%%")
plt.show()
#plt.savefig("臺北捷運104至108年總運量比例_圓餅圖.png")

# 全線圖
plt.figure(figsize=(8,6),dpi=100)
for i in range(0,5):
     plt.plot(xyear, pop[i], color=color[i], label=lbl[i])
plt.title("臺北捷運各路線年度進出站人次圖")
plt.ylabel("人次(億)")
plt.legend(loc='upper right')
plt.show()
#plt.savefig("臺北捷運各路線年度進出站人次圖_全線圖.png")

# 各自圖
plt.figure(figsize=(10,10),dpi=90)
for i in range(0,5):
     plt.subplot(3,2,i+1)
     plt.plot(xyear, pop[i], color=color[i])
     plt.ylabel("人次(億)")
     plt.title(lbl[i], y=1.0, pad=-14)
plt.show()
#plt.savefig("臺北捷運各路線年度進出站人次圖_各線圖.png")


