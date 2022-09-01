import requests
import pandas as pd
url = "https://rate.bot.com.tw/xrt/all/2021-07-29"
resp = requests.get( url )
if resp.status_code == 200:
    df = pd.read_html( resp.text )
    print(df)
    
df = pd.read_html('20210729匯率.html')
df = df[0]
df = df.iloc[:, :-3]
df.columns=['幣別,現金買入,'現金賣出,即期買入,即期賣
出']
df['mid']= df['幣別'].str.split('
').str[1].str.replace('(', '').str.replace(')','')
df['幣別']=df[幣別'].str.spli(.str[
df = df,set_index('mid')
for i in range(1,5):
df.iloc[:,i] = pd.to_numeric( df.iloc[:,i],errors='coerce')