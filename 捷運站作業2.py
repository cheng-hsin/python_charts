import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np

# url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"
# resp = requests.get( url )
#resp.encoding = 'utf-8'
# if resp.status_code == 200:
#      with open("腸病毒.csv","w", encoding="utf-8") as fobj:
#           fobj.write( resp.text )


df = pd.read_csv('TPMRT_P2.csv', encoding = 'utf-8')
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
xyear = df['年別']
ypeople = df.groupby('年別')['BR','G','R','BL','O'].sum()
plt.plot( xyear, ypeople ,label=ypeople)
plt.xlabel("年別")
plt.ylabel("人次")
plt.grid
plt.show()
print(df)
