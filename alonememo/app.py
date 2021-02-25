from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html');


@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾아서 가져오기 & _id 값은 출력에서 제외하기
    articles = list(db.articles.find({}, {'_id': False}))
    # 여기서 첫번째 articles : 서버쪽 변수. 두번째 괄호안 articles : db의 컬렉션이름

    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'articles': articles})
    # 여기서 articles는 내려주는 key값 ( client가 articles 안에 무슨 데이터가 있나를 찾아보는 것), 두번째껀 위에서 쓴 서버쪽 변수



## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])  # /memo라는 url이 html어디서 ajax콜을 하고있는지 확인하기 --> postArticle이라는 함수로 ajax call
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    # 2. meta tag를 스크래핑하기

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']

    # 3. mongoDB에 데이터 넣기
    doc = {
        'title': title,
        'image': image,
        'description': desc,
        'comment':comment_receive,
        'url':url_receive
    }

    db.articles.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
