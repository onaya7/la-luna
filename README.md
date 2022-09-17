#   Auth system

A Login system  built with Flask Perform User authentication and stores user data in Database (SQLite)

## How to run this application locally

To install all the packages, run:

```
pip3 install -r requirements.txt

```

create a .flaskenv and include:

```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=TRUE

```



create a .env and include:

```
SECRET_KEY = "your secret key"
DEBUG = 1
MAIL_SERVER = 'smtp.mailtrap.io'
MAIL_PORT =   2525
MAIL_USE_TSL= 1
MAIL_USE_SSL= 0
MAIL_USERNAME='your username'
MAIL_PASSWORD='your password'
MAIL_DEFAULT_SENDER= 'defautname@gmail.com'

```


Then run:

```
flask run

```

​
## Resources
-   Flask Documentation
https://flask.palletsprojects.comn/2.x/

-   Flask/SQLAlchemy documentation
https://flask-sqlalchemy.palletsprojects.com/en/2.x/

