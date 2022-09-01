import requests
from bs4 import BeautifulSoup

url = "https://udn.com/news/index"

resp = requests.get(url)

if resp.status_code == 200:
     soup = BeautifulSoup(resp.text,'html.parser')
     h3list = soup.find('section', 'article-list').find_all('h3', 'title')

     count=0
     with open('中時link.csv', 'w', encoding='utf-8-sig') as fobj:
          for i in h3list:
               count += 1
               fobj.write(i.text + ',' +i.a['href'])
               fobj.write('\n')
          print('共', count, '個')


     
