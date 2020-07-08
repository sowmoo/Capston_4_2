import requests #html 정보를 request하여 response할수있는 모듈
from bs4 import BeautifulSoup #request한 정보 html형식을 python에서는 지원하지 않기 때문에 BeautifulSoup를 사용하여 알맞게 맞춤 
import ssl  #default context파일을 위한 ssl모듈 
import pymysql #mysql 사용을 위한 모듈 
import re #텍스트 정렬을 위한 모듈
ssl._creat_default_https_context = ssl._create_unverified_context #https 통신시 ssl인증에 대한 context 파일을 일회성으로 인증받을수있음 

session = requests.Session() #request시 html의 session을 저장 
headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
       'Accpt':'text/html, application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8'
} #robot.txt파일의 header파일을 인가되어진 파일인지 검사를 하는데 request 모듈에서는 이를 조작할수있음 


cur = con.cursor()
sql = "select * from test"
cur.execute(sql)
data = cur.fetchall()

login_info = { #mysql 주소, 상수가 아닌 변수를 사용하려 하였으나 어플리케이션 백앤드 작업이 실패하면서 상수로 두었음 
       'class': data[1][5],
       'usr_id': data[1][2],
       'usr_pwd':data[1][3]
}

url = 'http://clc.chosun.ac.kr/ilos/lo/login.acl' #login 액션버튼 주소 학교측에서 정말 꽁꽁숨겨둬서 제이쿼리 8천줄 정독함 

with session as s:
      req = session.get(url, headers=headers,data=login_info)
       print(req.status_code)
       
       html = s.get('http://clc.chosun.ac.kr/ilos/mp/notification_list.cal') #과제정보를 저장하는 clc사이트 내부주소 
       soup = BeautifulSoup(html.text,'html.parser') #가져온 데이터를 BeautifulSoup로 다져줌 
       
       my_titles = soup.find_all("div") #다져진 형식에서 "div"클래스를 추출함 
       
       f = open('chosun/'+(' '.join(data[1][0])+'.txt'), mode= 'wt', encoding='utf-8') #텍스트 에디터에 저장할것인데 utf-8로 포맷형식을 맞추고 텍스트사이의 불필요한 공백제거 
       
       for i in range(len(my_titles)):
              data = (' '.join(my_titles[i].text).replace(" ","").replace("\n",""),'\n')
              f.write('\n'.join(data))
              
f.close()
con.close()      
       
