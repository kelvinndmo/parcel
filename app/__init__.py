from flask import Flask
from flask_restful import Api
from instance.config import app_config
from flask_jwt_extended import JWTManager
from .customer.customer_views import PostParcel, GetOrders, SpecificOrder, InTransitOrders, GetAcceptedOrders, DeclinedOrders, CompletedOrders



jwt = JWTManager()


def create_app(config_stage):
    '''creates the app'''

    app = Flask(__name__)
    app.config.from_object(app_config[config_stage])

    jwt.init_app(app)


    api = Api(app)

 
    api.add_resource(SpecificOrder, '/api/v1/orders/<int:id>')
    api.add_resource(PostParcel, '/api/v1/placeorder/orders')
    api.add_resource(GetOrders, '/api/v1/orders')
    api.add_resource(GetAcceptedOrders, '/api/v1/acceptedorders')
    api.add_resource(CompletedOrders, '/api/v1/orders/completedorders')
    api.add_resource(DeclinedOrders, '/api/v1/orders/declined')
    api.add_resource(InTransitOrders, '/api/v1/orders/intransit')

    return app
