"""app/feedback/views/feedback.py
"""

from flask import Blueprint, jsonify, redirect, request, url_for

from feedback.common.utility import err_response
from feedback.models.models import testmodel
from feedback.models import db
from flask_sqlalchemy import SQLAlchemy

feedback = Blueprint('feedback', __name__, url_prefix='/feedback')

@feedback.route('/healthcheck', methods=['GET'])
def healthcheck():
    """healthcheck
    """
    return jsonify({
        'status': 'healthy'
    }), 200

@feedback.route('/test', methods=['GET'])
def test_get():
    """test_get
    """
    payload = {
        "message": "これはテストです。"
    }
    return jsonify(payload), 200

#get
@feedback.route('/list', methods=['GET'])
def list_get():
    """list_get
    """
    lists = testmodel.query.all()
    return jsonify([list.to_dict() for list in lists]), 200

#post
@feedback.route('/post', methods=['GET'])
def post():
    """post
    """
    data = testmodel('五郎',5)
    db.session.add(data)
    db.session.commit()
    return jsonify(200), 200

@feedback.route('/post', methods=['POST'])
def post_post():
    """post_post
    """
    data = request.json
    print(data)
    data = testmodel(data['name'],data['age'])
    db.session.add(data)
    db.session.commit()
    return jsonify(200), 200

#update
@feedback.route('/update', methods=['GET'])
def update():
    """update
    """
    data = testmodel.query.filter_by(id=1).first()
    data.name = '太郎'
    data.age = 10
    db.session.commit()
    return jsonify(200), 200

#delete
@feedback.route('/delete', methods=['DELETE'])
def delete():
    """delete
    """
    data = request.json
    data = testmodel.query.get(data['id'])
    db.session.delete(data)
    db.session.commit()
    return jsonify(200), 200

@feedback.errorhandler(404)
@feedback.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code