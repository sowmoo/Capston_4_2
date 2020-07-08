import requests #request요청하여 html text들을 전부 가져옴 
from bs4 import BeautifulSoup #python의 형식에는 맞지 않는 형식이라 BeautifulSoup를 사용하여 python에 맞게 형식 맞춤 

request = requests.get('http://www.chosun.ac.kr/user/indexSub.do?codyMenuSeq=339072&siteId=scho') #크롤링할 주소 request 요청 
html = request.text 

soup = BeautifulSoup(html, 'html.parser') #python형식에 맞게 다져줌 

my_titles = soup.select('#list_frm > table > tbody') #다져진형식에서 #list_frm > table > tbody 부분만 추출

for title in my titles: #추출한 데이터 txt파일을 따로 생성하여 utf-8로 포맷형식을 맞추고 저장 (없으면 새로생성) 
       f = open('chosun/chosun_money.txt',mode='wt',encoding='utf-8') 
       subject = title.find_all('td',{'class':'title'})
       for i in range(len(subject)) :
              data = str(i+1)+') '+(' '.join(subject[i].text).replace(" ","").replace("\t","").replace("\n",""),'\n') #불필요한 공백제거 및 입맛에 맞춰서 다시 재정렬 
              
              f.write('\n'.join(data))
       
       
f.close()         
