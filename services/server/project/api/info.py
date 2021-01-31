import os
from flask import Flask, Blueprint, jsonify, request
from project.api.models import Info
from project import create_app, db
from project.api import selenium
from project.api import send_to_line

# ?? Blueprintとは何か？databaseの情報をflaskに教えてあげる必要があるのか．
info_blueprint = Blueprint('info', __name__)
# app = create_app()

@info_blueprint.route('/confirm_status', methods=['GET'])
def confirm_status():
    people_status = selenium.get_status()
    message = "{}".format(status)
    send_to_line.send_message(message)
    return jsonify({
        'status': 'success',
        'message': people_status,
        'container_id': os.uname()[1]
    })

@info_blueprint.route('/ask_shoudoku', methods=['GET'])
def write_db():
    # DBのget（SQLのselect）は以下のようにする．
    data = db.session.query(Info.name, Info.count).all()
    counts = {}
    for d in data:
        counts[d[0]] = d[1]
    
    print("Kye", counts.keys())
    name = selenium.decide_whom(counts)
    
    # TODO 仮
    # count = counts[name] + 1
    count = 10
    
    message = "{}さん本日の消毒と安全点検をお願いします".format(name)
    print(message)

    # DBへの書込み
    # TODO
    # db.session.query(Info).filter(Info.name == name).first().count = count
    # db.session.commit()

    send_to_line.send_message(message)
    return jsonify({
        'status': 'success',
        'message': message,
        'container_id': os.uname()[1]
    })

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

if __name__ == '__main__':
    app.run()