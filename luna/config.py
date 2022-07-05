import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = bool(os.getenv('DEBUG'))
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')  
    MAIL_USE_TSL= bool(os.getenv('MAIL_USE_TSL'))
    MAIL_USE_SSL= bool(os.getenv('MAIL_USE_SSL'))
    MAIL_USERNAME=os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER= os.getenv('MAIL_DEFAULT_SENDER')
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'data.sqlite') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

