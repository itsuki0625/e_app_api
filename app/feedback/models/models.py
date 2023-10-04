"""app/feedback/models/models.py
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db

#CREATE TABLE testmodel (id INT PRIMARY KEY , name TEXT NOT NULL, email VARCHAR(255) UNIQUE);
class Movies(db.Model):
    __tablename__ = 'movies'
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False) #動画タイトル
    description = db.Column(db.String(255), nullable=False) #動画説明
    thumbnail_url = db.Column(db.String(255), nullable=False) #サムネイルURL
    movie_url = db.Column(db.String(255), nullable=False) #動画URL
    short_movie_url = db.Column(db.String(255), nullable=False) #short動画URL
    short_movie_counter = db.Column(db.Integer, nullable=False) #short動画再生回数
    buy_counter = db.Column(db.Integer, nullable=False) #購入回数
    auther_id = db.Column(db.Integer, nullable=False) #投稿者
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }