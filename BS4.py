import requests
from bs4 import BeautifulSoup

url = "https://udn.com/news/index"

resp = requests.get(url)

if resp.status_code==200:
     #print(resp.text)

     soup = BeautifulSoup(resp.text, 'html.parser')
     alist=soup.find_all('a',{'class':'tab-link'})
     
     for i in alist:
          try:
               if ':' not in i.span.text:
                    print(i.text,i['href'])
          except:
               print(i.text,'沒有連結網址@@@@@@@@@@@@@@@@@@@@@@@')
               
