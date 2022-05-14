from . import db



class Quotes:
    def __init__(self,quote,author):
        self.quote = quote
        self.author = author

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')

    
    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__="blogs"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Blog {self.title}'
   

   

    