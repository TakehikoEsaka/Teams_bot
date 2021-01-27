from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import Info
from project.api import info
from flask_apscheduler import APScheduler
import json
import os

app = create_app()
cli = FlaskGroup(create_app=create_app)

def before():
    print("おはようございます．今日の勤怠状況をwhite-boardの記入をお願いします")

def after():
    print("お疲れ様です．明日の勤怠の予定をwhite-boardへ記入をお願いします")

def now(name, count):
    # app_contextのwithステートメントの中で記述が必要
    with app.app_context():
        info.write_db()

    # 投稿
    # curl -H 'Content-Type: application/json' -d '{"text": "Hello World"}' <YOUR WEBHOOK URL>

# python manage.pyの引数をここで定義
@cli.command('recreate_db')
def recreate_db():
    # データベースを操るcursorはflaskインスタンスから，db = SQLAlchemy(app)と生成する事が一般的
    db.drop_all() # 既存のdatabase削除
    db.create_all() # 作成したクラス(テーブル)を実際にSQLite上に作成
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    names = os.getenv("PEOPLE_NAME").split(",")
    for n in names:
        db.session.add(Info(name=n, count=0, status=False)) # dbにエントリをaddする
    db.session.commit()

if __name__ == '__main__':
    scheduler = APScheduler()
    # FLASK_ENVがdevelopmentの時はfuncが2回送信されるので注意
    scheduler.add_job(func=before, args=[], trigger='interval', id='before', seconds=60)
    # scheduler.add_job(func=now, args=["榎阪", 200], trigger='interval', id='now', seconds=60)
    scheduler.add_job(func=after, args=[], trigger='interval', id='after', seconds=60)
    scheduler.start()
    cli()