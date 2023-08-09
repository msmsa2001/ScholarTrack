from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    global app
    app=Flask(__name__)
    
    app.config["SECRET_KEY"]="QWERTYUIOasdfghjkwertsdgsfh"
    app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:root@localhost/students'

    db.init_app(app)


    from app.auth.controllers import auth_blueprint

    app.register_blueprint(
        auth_blueprint,
        url_prefix=f'/api/{auth_blueprint.url_prefix}'  
        )
    
    from app.common.controllers import common_blueprint

    app.register_blueprint(
        common_blueprint,
        url_prefix=f'/api/{common_blueprint.url_prefix}'  
        )
    
    return app


