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



df = pd.read_csv('北捷代號.csv', encoding = 'big5')
column=["BR總","R總","G總","BL總","O總"]
dfTotal=df.groupby(['年別']).sum() 
print(df[['BR總','R總','G總','BL總','O總']])
print(dfTotal)






