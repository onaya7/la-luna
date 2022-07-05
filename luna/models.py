from datetime import datetime
from flask_login import UserMixin
from luna.instance import db ,login_manager





#user loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#user model
class  User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False)
    lastname = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.id}','{self.firstname}', '{self.lastname}', '{self.email}')"

#