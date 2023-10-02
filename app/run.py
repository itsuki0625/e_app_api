"""app/run.py
"""

import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from feedback.views.feedback import feedback
from feedback.common.utility import err_response
from feedback.models import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(feedback)

@app.errorhandler(404)
@app.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code

def main():
    """main
    """
    host = '0.0.0.0'
    port = 5555
    app.run(host=host, port=port)
    

if __name__ == '__main__':
    main()