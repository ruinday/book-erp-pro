from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .config import ORIGINS,METHODS

cors = CORS()
migrate = Migrate()
api = Api()
db = SQLAlchemy()

def init_exts(app):
    cors.init_app(app=app,origins=ORIGINS,methods=METHODS)
    migrate.init_app(app=app,db=db)
    api.init_app(app=app)
    db.init_app(app=app)