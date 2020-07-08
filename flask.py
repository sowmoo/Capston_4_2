from flask import Flask, request, jsonify
import pymysql
import sys
import re
from datetime import datetime
from random import randint

app = Flask(__name__, static_url_path='/static')

#데이터베이스에서 정보를 추출하여 카카오 오픈빌더로 전송해야함으로 mysql 접속 코드 
con = pymysql.connect(host='아마존 RDS서버 호스트명 ',
                                 port=3306,
                                 user='데이터베이스 유저명 ',
                                 passwd='비밀번호',
                                 db='데이터베이스 테이블명',
                                 charset='utf8')


@app.route('/message', methods=['POST','GET']) #카카오 오픈빌더에서 요청하고있는 기본형식  
def Message(): 
       req = request.get_json()
       req = req('userRequest']
       req = req['user']
       req = req['id']
       req = (' '.join(req)).replace(' ','')

       cur = con.cursor()
       sql = "select * from test"
       cur.execute(sql)
       data = cur.fetchasll()

       content = request.get_json()
       content = content['userRequest']
       content = content['utterance']

       if content == u'공지사항':

              f = open('sw_chosun.txt'.'r')
              dataSend = {
                     "version": "2.0",
                     "template": {
                            "outputs": [
                                   {
                                          "carousel":{
                                                 "type" : "basicCard",
                                                 "items": [
                                                        {
                                                               "title" : "",
                                                               "description" : " ".join(f.readlines())
                                                               }
                                                        ]
                                                 }
                                          }
                                   ]
                            }
                     }

       if content == u'장학금':

              f = open('chosun_money.txt'.'r')
              dataSend = {
                     "version": "2.0",
                     "template": {
                            "outputs": [
                                   {
                                          "carousel":{
                                                 "type" : "basicCard",
                                                 "items": [
                                                        {
                                                               "title" : "",
                                                               "description" : " ".join(f.readlines())
                                                               }
                                                        ]
                                                 }
                                          }
                                   ]
                            }
                     }
              elif content == u"과제":
                  if data[1][1] == req:
                      f = open((' '.join(data[1][0]))+'.txt','r')
                      dataSend = {
                           "version":"2.0",
                           "template":{
                                  "outputs":[
                                         {
                                                "carousel":{
                                                       "type" : "basicCard",
                                                       "items": [
                                                              {
                                                                     "title" : "",
                                                                     "description" : " ".join(f.readlines())
                                                                     }
                                                              ]
                                                       }
                                                }
                                         ]
                                  }
                            }
                            f.close
                     else :
                            dataSend = {
                                "version":"2.0",
                                "template":{
                                    "outputs":[
                                      {
                                          "carousel":{
                                              "type":"basicCard",
                                                  "items":[
                                                            {
                                                                "title": "",
                                                                "description" : "미등록 사용자입니다.\n\n새로 등록하시려면\n\해당 챗봇에서 인증번호를 부여받으신뒤 \n\n어플리케이션으로 로그인 해주세요."
                                                            }
                                                          ]
                                                  }
                                              }
                                         ]
                                    }
                              }
       elif content == u"인증번호":
              count = 0
              for i in range(0,len(data)):
                     if(data[i][1] == req):
                            count == 1
                            dataSend = {
                                   "version":"2.0",
                                   "template":{
                                          "outputs":[
                                                 {
                                                   
                                                        "carousel":{
                                                               "type" : "basicCard",
                                                               "items": [
                                                                      {
                                                                             "title" : "",
                                                                             "description" : "고객님은 등록되있는 상태입니다.\n\n인증번호는 %s입니다. ", %(data[i][4])
                                                                             }
                                                                      ]
                                                               }
                                                        }
                                                 ]
                                          }
                                   }
               if(count == 0):
                      random_number = randint(10000,99999)
                      cur = con.cursor()
                      sql_insert = """insert into test (number,user,key_number) values (%s, %s,%s)"""

                      cur.execute(sql_insert, (len(data)+1,req,random_number))
                      con.commit()

                      dataSend = {
                             "version":"2.0",
                                   "template":{
                                          "outputs":[
                                                 {
                                                        "carousel":{
                                                               "type" : "basicCard",
                                                               "items": [
                                                                      {
                                                                             "title" : "",
                                                                             "description" : "\b현재 등록되지 않은 사용자 입니다. 인증번호를 발급합니다. \n\n 인증번호 %s" , % (random_number)
                                                                             }
                                                                      ]
                                                               }
                                                        }
                                                 ]
                                          }
                                   }       
       return jsonify(dataSend)
       f.close()
       con.close()

@app.route('/app',methods = ['POST','GET'])
def App():
       user = request.get_json()
       print(user)


if __name__ == "__main__":
       app.run(host='0.0.0.0', port = 5000)
