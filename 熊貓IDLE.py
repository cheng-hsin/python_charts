import pandas as pd
import requests


from io import StringIO
url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"
resp = requests.get( url )
resp.encoding = 'utf-8'
df = pd.read_csv( StringIO(resp.text) )

print(df.groupby('縣市')['健保就診總人次'].min())



'''
df = pd.read_csv('NHI_EnteroviralInfection.csv')
df1 = df[ (df['縣市']=='台北市')&(df['年齡別']=='0-2') ]
print(df1)
'''



