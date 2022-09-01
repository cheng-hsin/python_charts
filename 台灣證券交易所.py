import requests
import pandas as pd
from io import StringIO
import sqlite3
import time

conn = sqlite3.connect('twstock.sqlite3')
d = pd.date_range('20180101', '20210601', freq='M')
print(d)
for i in d:
     d1 = str(i)[:10].replace('-','')

     url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date="+d1+"&stockNo=2330"
     print(url)
     time.sleep(10)
     resp = requests.get(url)

     if resp.status_code == 200:

          clist = resp.text.split('\n')
          slist = []
          for i in clist :
               if len(i.split('",')) == 10:
                    slist.append(i)

          content = '\n'.join(slist)
          df = pd.read_csv(StringIO(content) )
          df = df.iloc[:, :9]
          #print(content)

          for i in [1,2,8]:
               df.iloc[:, i] = df.iloc[:, i].str.replace(',','')
               df.iloc[:, i] = pd.to_numeric( df.iloc[:,i], errors='coerce')
          df = df.set_index('日期')
          df.to_sql('s2330', conn, if_exists='append')



