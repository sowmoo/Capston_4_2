import requests
from bs4 import BeautifulSoup

request = requests.get('http://www.chosun.ac.kr/user/indexSub.do?codyMenuSeq=339072&siteId=scho')
html = request.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select('#list_frm > table > tbody')

for title in my titles:
       f = open('chosun/chosun_money.txt',mode='wt',encoding='utf-8')
       subject = title.find_all('td',{'class':'title'})
       for i in range(len(subject)) :
              data = str(i+1)+') '+(' '.join(subject[i].text).replace(" ","").replace("\t","").replace("\n",""),'\n')
              
              f.write('\n'.join(data))
            
       
f.close()         
