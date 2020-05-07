from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):

    '''
    callback function retrieves user when unique identifier is passed
    '''
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):

    '''
    class facilitates the creation of user objects
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_photo_pic = db.Column(db.String())
    role_id = (db.Column(db.Integer,db.ForeignKey('roles.id')))
    password_hash = db.Column(db.String)

    @property
    def password(self):

        '''
        function raises AttributeError to prevent access to password property
        '''
        raise AttributeError('You cannot access password property')

    @password.setter
    def password(self,password):

        '''
        function generates password has and saves it to the database
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):

        '''
        function takes entered password hashes it and compares the newly hashed password with the hashed password saved in the database
        '''
        return check_password_hash(self.password_hash,password)



    def __repr__(self):

        '''
        function eases debugging
        '''
        return f'User {self.username}'

class Role(db.Model):

    '''
    model facilitates the creation of role objects
    '''
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(255))
    users = db.relationship('User',backref='role',lazy="dynamic")

    def __repr__(self):
        
        '''
        function promotes debugging
        '''
        return f'User {self.name}'