import requests #request용 모듈 
from bs4 import BeautifulSoup #response된 html문장들을 python형식에 맞춰 다져줌 

request = requests.get('http://sw.chosun.ac.kr/boardList.do?pageId=www42&boardId=NOTICE') #크롤링 주소 
html = request.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select('#skip.content > div.content > div.siiru-boardWrap > div.board_list > div.board_list_body')  #다져진 전체html문장중 추출주소 

for title in my titles:
       f = open('chosun/sw_chosun.txt',mode='wt',encoding='utf-8')
       date = title.find_all('div',{'class':'date'})
       subject = title.find_all('div',{'class':'subject'})
       
       for i in range(len(subject)):
              data = str(i+1)+') '+(' '.join(subject[i].text).replace(" ","").replace("\n",""),'\n')
              f.write('\n'.join(data))
              
              
f.close()
