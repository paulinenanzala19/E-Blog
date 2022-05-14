from . import db
from werkzeug.security import generate_password_hash,check_password_hash



class Quotes:
    def __init__(self,quote,author):
        self.quote = quote
        self.author = author

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__="blogs"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Blog {self.title}'
   

   

    