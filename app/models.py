from . import db
from werkzeug import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),nullable=False,unique=True)
    email = db.Column(db.String(255),nullable=True,unique=True)
    password = db.Column(db.String(255),nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self,password):
        password_hash = generate_password_hash(password)
        self.password = password_hash
    def __repr__(self):
        return f'User{self.username}'
