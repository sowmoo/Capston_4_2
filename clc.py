import requests
from bs4 import BeautifulSoup
import ssl
import pymysql
import re
ssl._creat_default_https_context = ssl._create_unverified_context

session = requests.Session()
headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
       'Accpt':'text/html, application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8'
}


cur = con.cursor()
sql = "select * from test"
cur.execute(sql)
data = cur.fetchall()

login_info = {
       'class': data[1][5],
       'usr_id': data[1][2],
       'usr_pwd':data[1][3]
}

url = 'http://clc.chosun.ac.kr/ilos/lo/login.acl'

with session as s:
      req = session.get(url, headers=headers,data=login_info)
       print(req.status_code)
       
       html = s.get('http://clc.chosun.ac.kr/ilos/mp/notification_list.cal')
       soup = BeautifulSoup(html.text,'html.parser')
       
       my_titles = soup.find_all("div")
       
       f = open('chosun/'+(' '.join(data[1][0])+'.txt'), mode= 'wt', encoding='utf-8')
       
       for i in range(len(my_titles)):
              data = (' '.join(my_titles[i].text).replace(" ","").replace("\n",""),'\n')
              f.write('\n'.join(data))
              
f.close()
con.close()      
       
