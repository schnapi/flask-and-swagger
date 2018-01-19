#from flask import Flask, Blueprint, url_for
#from flask_restplus import Api
#
#app = Flask(__name__)
##app.config.SWAGGER_UI_JSONEDITOR = True
##app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
##app.config.SWAGGER_UI_LANGUAGES = ['en', 'fr']
#blueprint = Blueprint('api', __name__, url_prefix='/api')
#api = Api(blueprint, doc='/doc/')
#
# app.register_blueprint(blueprint)
#
#assert url_for('api.doc') == '/api/doc/'
from flask import Flask
from apis import api
from logging.handlers import RotatingFileHandler
import logging
from database import db

app = Flask(__name__)
api.init_app(app)

Host = "localhost"
User = 'root'
Password = 'root'
DB = 'petdb'
Charset = 'utf8mb4'

if __name__ == '__main__':
    handler = RotatingFileHandler('log.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    db.init(Host, User, Password, DB, Charset)
    app.run(debug=True)
