from . import db
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer  # Updated import
from flask import current_app
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"<User {self.email}>"




class ChangeOwnershipFormModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cemetery = db.Column(db.String(100), nullable=False)
    block_number = db.Column(db.String(50), nullable=False)
    grave_space = db.Column(db.String(50), nullable=False)
    owner_details = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    name_1 = db.Column(db.String(100), nullable=True)
    address_1 = db.Column(db.String(200), nullable=True)
    signature_1 = db.Column(db.String(50), nullable=True)
    id_number_1 = db.Column(db.String(20), nullable=True)
