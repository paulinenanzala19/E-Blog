from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin



class Quotes:
    def __init__(self,quote,author):
        self.quote = quote
        self.author = author

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    upvote=db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote=db.relationship('Downvote',backref='user',lazy='dynamic')
    comment=db.relationship('Comments',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


    
    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__="blogs"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post = db.Column(db.Text(), nullable = False)
    upvote=db.relationship('Upvote',backref='blog',lazy='dynamic')
    downvote=db.relationship('Downvote',backref='blog',lazy='dynamic')
    comment=db.relationship('Comments',backref='blog',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Blog {self.title}'

class Upvote(db.Model):
    __tablename__='upvotes'

    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   


    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes = cls.query.filter_by(blog_id=id).all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

class Downvote(db.Model):
    __tablename__='downvotes'

    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvotes = cls.query.filter_by(blog_id=id).all()
        return downvotes

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.Column(db.Text(),nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comments.query.filter_by(blog_id=blog_id).all() 

        return comments 

    def __repr__(self):
        return f'comment:{self.comment}'

   

   

    