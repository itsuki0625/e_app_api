"""app/feedback/models/models.py
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db

#CREATE TABLE testmodel (id INT PRIMARY KEY , name TEXT NOT NULL, email VARCHAR(255) UNIQUE);
class testmodel(db.Model):
    __tablename__ = 'testmodel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
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