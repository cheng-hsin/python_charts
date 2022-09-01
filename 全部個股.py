import requests
import pandas as pd
from io import StringIO
import sqlite3
import time

conn = sqlite3.connect('twstock.sqlite3')

url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=JSON&date=20210803&type=ALLBUT0999"
print(url)
resp = requests.get(url)

if resp.status_code == 200:
     print(resp.text)
     with open("全部個股.txt","w", encoding="utf-8") as fobj:
          fobj.write( resp.text )
            


'''
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
'''
