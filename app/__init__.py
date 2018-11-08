from flask import Flask
from flask_restful import Api
from instance.config import app_config
from flask_jwt_extended import JWTManager
from .admin.admin_views import CompleteOrder, AcceptStatus, MarkOrderInTransit, DeclineOrder



jwt = JWTManager()


def create_app(config_stage):
    '''creates the app'''

    app = Flask(__name__)
    app.config.from_object(app_config[config_stage])

    jwt.init_app(app)


    api = Api(app)

    api.add_resource(CompleteOrder, '/api/v1/orders/<int:id>/completed')
    api.add_resource(AcceptStatus, '/api/v1/orders/<int:id>/approved')
    api.add_resource(MarkOrderInTransit, '/api/v1/orders/<int:id>/intransit')
    api.add_resource(DeclineOrder, '/api/v1/orders/<int:id>/declined')

    return app
