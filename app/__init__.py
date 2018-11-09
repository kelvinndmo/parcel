from flask import Flask
from flask_restful import Api
from instance.config import app_config
from flask_jwt_extended import JWTManager
<<<<<<< HEAD
from .admin.admin_views import CompleteOrder, AcceptStatus, MarkOrderInTransit, DeclineOrder

=======
<<<<<<< HEAD
from app.auth.auth_views import Login, SignUp
=======
from .customer.customer_views import PostParcel, GetOrders, SpecificOrder, InTransitOrders, GetAcceptedOrders, DeclinedOrders, CompletedOrders

>>>>>>> a8686befc68819fa446d8017cf2d5ee07641ef1c
>>>>>>> challenge-tw-develop


jwt = JWTManager()


def create_app(config_stage):
    '''creates the app'''

    app = Flask(__name__)
    app.config.from_object(app_config[config_stage])

    jwt.init_app(app)


    api = Api(app)

<<<<<<< HEAD
    api.add_resource(CompleteOrder, '/api/v1/orders/<int:id>/completed')
    api.add_resource(AcceptStatus, '/api/v1/orders/<int:id>/approved')
    api.add_resource(MarkOrderInTransit, '/api/v1/orders/<int:id>/intransit')
    api.add_resource(DeclineOrder, '/api/v1/orders/<int:id>/declined')
=======
<<<<<<< HEAD
    api.add_resource(SignUp, '/api/v1/auth/signup')
    api.add_resource(Login, '/api/v1/auth/login')
    
=======
 
    api.add_resource(SpecificOrder, '/api/v1/orders/<int:id>')
    api.add_resource(PostParcel, '/api/v1/placeorder/orders')
    api.add_resource(GetOrders, '/api/v1/orders')
    api.add_resource(GetAcceptedOrders, '/api/v1/acceptedorders')
    api.add_resource(CompletedOrders, '/api/v1/orders/completedorders')
    api.add_resource(DeclinedOrders, '/api/v1/orders/declined')
    api.add_resource(InTransitOrders, '/api/v1/orders/intransit')
>>>>>>> a8686befc68819fa446d8017cf2d5ee07641ef1c
>>>>>>> challenge-tw-develop

    return app
