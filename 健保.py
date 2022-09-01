import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np

# url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"
# resp = requests.get( url )
# resp.encoding = 'utf-8'
# if resp.status_code == 200:
#      with open("腸病毒.csv","w", encoding="utf-8") as fobj:
#           fobj.write( resp.text )



df = pd.read_csv('腸病毒.csv')
# xyear = np.arange(df['年'].min(),df['年'].max()+1)
xyear = sorted(set(df['年']))
ypeople = df.groupby('年')['健保就診總人次'].sum()

# plt.plot( xyear, ypeople )
# plt.grid
# plt.show()


# city = set( df['縣市'])
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# for c in city:
#     ypeople= df[ df['縣市']==c].groupby('年')['健保就診總人次'].sum()
#     plt.plot(xyear,ypeople,label=c)
#     plt.legend()
# plt.show()


s1=df.groupby('縣市')['健保就診總人次'].mean()
s2 = s1.sort_values(ascending=False)

plt.subplot(2,2,1)
for c in s2[:4].index:
    ypeople = df[df['縣市'] == c].groupby('年')['健保就診總人次'].sum()
    plt.plot(xyear,ypeople,label=c)
plt. legend()

plt.subplot(2,2,2)
for c in s2[4:9].index:
    ypeople = df[df['縣市'] == c].groupby('年')['健保就診總人次'].sum()
    plt.plot(xyear, ypeople, label=c)
plt. legend(loc='lower left')

plt.subplot(2,2,3)
for c in s2[9:-4].index:
    ypeople = df[df['縣市'] == c].groupby('年')['健保就診總人次'].sum()
    plt.plot(xyear, ypeople, label=c)
plt. legend(loc='lower left')

plt.subplot(2,2,4)
for c in s2[-4:].index:
    ypeople = df[df['縣市'] == c].groupby('年')['健保就診總人次'].sum()
    plt.plot(xyear, ypeople, label=c)
plt. legend(loc='lower left')
plt.show()