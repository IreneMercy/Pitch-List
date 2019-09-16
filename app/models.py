from datetime import datetime
from . import db,loginmanager
from werkzeug import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=True,unique=True)
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return f'User{self.username}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self,password):
        password_hash = generate_password_hash(password)
        self.password = password_hash

    def check_password(self,password):
        return check_password_hash(self.password,password)



    @loginmanager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String(50),nullable=False)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
