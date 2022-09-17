from flask import Flask
from luna.models import login_manager
from luna.config import Config
from luna.routes import users
from luna.webhook import data
from luna.instance import db, bcrypt, mail, login_manager




def create_app(config_class=Config):
    # Creating an instance of flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # initializing db 
    db.init_app(app)

    # initializing bcrypt
    bcrypt.init_app(app)

    # initializing flask_login
    login_manager.init_app(app)
    login_manager.login_view="users.login"
    login_manager.login_message='You dont have access to this page'

    #initializing flask-mail
    mail.init_app(app)
    

    #Blueprint views
    app.register_blueprint(users)
    app.register_blueprint(data)
    return app














































# def create_app(config_name):
#     app= Flask(__name__)
   
#     app.config.from_object(config[config_name])   
#     config[config_name].init_app(app)
   


    
#     # creating an SQLAlchemy instance
#     db.init_app(app)
#     db.create_all()

   

#     return app

