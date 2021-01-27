import os

from flask import Blueprint, jsonify, request
from project.api.models import Info
from project import db
from project.api import selenium

# ?? Blueprintとは何か？databaseの情報をflaskに教えてあげる必要があるのか．
info_blueprint = Blueprint('info', __name__)

def write_db():
    # DBのget（SQLのselect）は以下のようにする．
    data = db.session.query(Info.name, Info.count).all()
    counts = {}
    for d in data:
        counts[d[0]] = d[1]
    
    name = selenium.decide_whom(counts)
    count = counts[name] + 1
    message = "{}さん本日の消毒と安全点検をお願いします".format(name)
    print(message)

    # DBへの書込み
    db.session.query(Info).filter(Info.name == name).first().count = count
    db.session.commit()

    return message

# APIサーバーのURLをここで指定
@info_blueprint.route('/info', methods=['GET', 'POST'])
def all_info():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    if request.method == 'POST':
        # post_data = request.get_json() # json dataが入っている．
        # status = post_data.get('status')
        write_db()
        response_object['message'] = 'Information Added'
    else:
        # infoテーブルの全データを取得
        response_object['info'] = [info.to_json() for info in Info.query.all()]
    return jsonify(response_object)

@info_blueprint.route('/info/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })

# blue_printによってパスの書き方が変わるのはなぜか??
# @books_blueprint.route('/books/<book_id>', methods=['PUT', 'DELETE'])
@info_blueprint.route('/info/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {
      'status': 'success',
      'container_id': os.uname()[1]
    }
    book = Book.query.filter_by(id=book_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        book.title = post_data.get('title')
        book.author = post_data.get('author')
        book.read = post_data.get('read')
        db.session.commit()
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()