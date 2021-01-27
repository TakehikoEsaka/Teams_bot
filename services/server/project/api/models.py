import datetime

from flask import current_app
from sqlalchemy.sql import func

from project import db

# SQLAlchemyはクラス名を見て自動的にtableを作ってくれる．
# Bookなら -> bookテーブルを作成
class Info(db.Model):

    __tablename__ = 'info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(255), nullable=True)
    
    def __init__(self, name, count, status):
        self.name = name
        self.count = count
        self.status = status

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'count': self.count,
            'status': self.status
        }