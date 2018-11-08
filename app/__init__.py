from flask import Flask
from flask_restful import Api
from instance.config import app_config
from flask_jwt_extended import JWTManager
from app.auth.auth_views import Login, SignUp


jwt = JWTManager()


def create_app(config_stage):
    '''creates the app'''

    app = Flask(__name__)
    app.config.from_object(app_config[config_stage])

    jwt.init_app(app)


    api = Api(app)

    api.add_resource(SignUp, '/api/v1/auth/signup')
    api.add_resource(Login, '/api/v1/auth/login')
    

    return app
