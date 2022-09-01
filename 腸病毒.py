import pandas as pd
import matplotlib.pyplot as plt
import requests
'''
url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"
resp = requests.get( url )
resp.encoding = 'utf-8'
if resp.status_code == 200:
     with open("腸病毒.csv","w", encoding="utf-8") as fobj:
          fobj.write( resp.text )

print(content[:1000])
'''

df = pd.read_csv('腸病毒.csv')


