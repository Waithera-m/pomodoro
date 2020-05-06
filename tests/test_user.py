import unittest
from app.models import User

class TestUser (unittest.TestCase):

    '''
    class facilitates the creation of testcases to test User class behavior
    '''
    def setUp(self):
        
        '''
        function runs before each test case
        '''
        self.new_user = User(password="allonsy")
        
    def test_password_setter(self):

        '''
        function checks if password is hashed
        '''
        self.assertTrue(self.password_hash is not None)

    def test_password_access(self):

        '''
        function checks if attempts to access password property raise AttributeError
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_verification(self):

        '''
        function checks if app verifies hashed passwords
        '''
        self.assertTrue(self.new_user.verify_password('allonsy'))