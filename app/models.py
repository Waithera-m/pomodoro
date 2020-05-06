from . import db
from werkzeug.seurity import generate_password_hash,check_password_hash

class User(db.Model):

    '''
    class facilitates the creation of user objects
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)
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
        return check_password_hash(self.password_hash,pasword)



    def __repr__(self):

        '''
        function eases debugging
        '''
        return f'User {self.username}'