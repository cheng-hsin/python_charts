import requests
import pandas as pd
from io import StringIO
import sqlite3

conn = sqlite3.connect('twstock.sqlite3')

#url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20210803&type=ALLBUT0999"

#resp = requests.get(url)

#if resp.status_code == 200:
#     with open('stock20210803.csv','w', encoding='utf-8') as fobj:
#          fobj.write(resp.text)
#     print(resp.text)

with open('stock20210803.csv', 'r',encoding='utf-8') as fobj:
     content = fobj.read()

clist = content.split('\n')
slist = []
for i in clist:
     #print(len(i.split('",')))

     if len(i.split('",')) == 17:
          slist.append(i)
content = '\n'.join(slist)
df = pd.read_csv(StringIO(content))
df=df.iloc[:,:16]
df['證券代號'] = df['證券代號'].str.replace('=', '').str.replace('"', '')
for i in [2,3,4,5,6,7,8,11,12,13,14,15]:
     df.iloc[:,i] = df.iloc[:,i].str.replace(',','')
     df.iloc[:,i] = pd.to_numeric(df.iloc[:,i],errors='coerce')

df['日期'] = '20210803'
df.to_sql('allstock', conn, if_exists='append')
print(df)
