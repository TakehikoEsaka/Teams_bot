import os
from flask import Flask, Blueprint, jsonify, request
from project.api.models import Info
from project import create_app, db
from project.api import selenium

# ?? Blueprintとは何か？databaseの情報をflaskに教えてあげる必要があるのか．
info_blueprint = Blueprint('info', __name__)
# app = create_app()

# @info_blueprint.route('/confirm_status', methods=['GET'])
def confirm_status():
    status = selenium.get_status()
    return jsonify({
        'status': 'success',
        'message': status,
        'container_id': os.uname()[1]
    })

# @info_blueprint.route('/ask_shoudoku', methods=['GET'])
def write_db():
    # DBのget（SQLのselect）は以下のようにする．
    data = db.session.query(Info.name, Info.count).all()
    counts = {}
    for d in data:
        counts[d[0]] = d[1]
    
    print("Kye", counts.keys())
    name = selenium.decide_whom(counts)
    count = counts[name] + 1
    message = "{}さん本日の消毒と安全点検をお願いします".format(name)
    print(message)

    # DBへの書込み
    db.session.query(Info).filter(Info.name == name).first().count = count
    db.session.commit()

    return message

@info_blueprint.route('/info', methods=['GET'])
def all_info():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    response_object['info'] = [info.to_json() for info in Info.query.all()]
    return jsonify(response_object)

@info_blueprint.route('/info/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })

# @app.route('/hello')
@info_blueprint.route('/hello_nice', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, world'})

if __name__ == '__main__':
    app.run()