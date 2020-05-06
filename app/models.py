from . import db

class User(db.Model):

    '''
    class facilitates the creation of user objects
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):

        '''
        function eases debugging
        '''
        return f'User {self.username}'