from flask import Flask, render_template, jsonify, request
from bson.objectid import ObjectId #str인 _id를 obj로 변환
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('mongodb://test:test@13.124.242.180', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbjungle  # 'dbjungle'라는 이름의 db를 만들거나 사용합니다.

@app.route('/')
def home():
    return render_template('index.html')

#메모 리스트 조회
@app.route('/list', methods=['GET'])
def read_memo():
    # 1. mongoDB에서 모든 데이터 조회해오기 (Read)
    result = obj_decode(list(db.memos.find({}).sort('like',-1)))
    # 2. memos라는 키 값으로 memos 정보 보내주기
    return jsonify({'result': 'success', 'memos': result})

#메모 입력 
@app.route('/create', methods=['POST'])
def post_memo():
    # 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['memo_title']  # 클라이언트로부터 title 받는 부분
    comment_receive = request.form['memo_comment']  # 클라이언트로부터 comment 받는 부분

    memo = {'title': title_receive, 'comment': comment_receive ,'like': 0}

    # 2. mongoDB에 데이터를 넣기
    db.memos.insert_one(memo)

    return jsonify({'result': 'success'})

#메모 수정
@app.route('/update', methods=['POST'])
def update_memo():
    obj_id = ObjectId(request.form['id'])
    title_receive = request.form['memo_title']  
    comment_receive = request.form['memo_comment'] 
    update_query = {'title' : title_receive, 'comment' : comment_receive}
    
    db.memos.update_one({'_id': obj_id}, {'$set': update_query})

    return jsonify({'result': 'success'})

#메모 좋아요
@app.route('/like', methods=['POST'])
def like_memo():
    obj_id = ObjectId(request.form['id'])
    db.memos.update_one({'_id': obj_id}, {'$inc': {'like': 1}})

    return jsonify({'result': 'success'})

#메모 삭제
@app.route('/delete', methods=['POST'])
def delete_memo():
    obj_id = ObjectId(request.form['id'])
    db.memos.delete_one({'_id': obj_id})

    return jsonify({'result': 'success'})

#오브젝트인 _id를 str으로 decode
def obj_decode(list):
    results = []
    for doc in list:
        doc['_id'] = str(doc['_id'])
        results.append(doc)
    return results

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)