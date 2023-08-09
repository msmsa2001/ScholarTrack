from flask_restful import Api
from flask import Blueprint

from app.auth.controllers.login import LoginView

auth_blueprint = Blueprint("auth",__name__,url_prefix="/auth")
api=Api(auth_blueprint)

api.add_resource(LoginView,"/login")