# Setting>Projectname>Python Interpreter가서 flask랑 pymongo깔아줘야함
#>pip install flask, >pip install pymongo
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분 ((Post&get. 타입이 다르면 함수이름(여기서 result)이 똑같아도 괜찮음.))
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # "DB에 insert하는 법 (Week3)"
    doc = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    db.bookreview.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니다.'})


@app.route('/review', methods=['GET'])
def read_reviews():
    title_receive = request.args.get('title_give')
    author_receive = request.args.get('author_give')
    review_receive = request.args.get('review_give')

    reviews = list(db.bookreview.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
