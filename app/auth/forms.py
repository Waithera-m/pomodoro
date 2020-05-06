from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField
from wtforms.validators import Email,Required,EqualTo
from ..models import User

class SignUpForm(FlaskForm):

    '''
    class facilitates the creation of sign up form objects
    '''
    email = StringField('Enter Your Email Address', validators=[Required(),Email()])
    username = StringField('Enter Your Username', validators=[Required()])
    password = StringField('Enter Your Password',validators=[Required(), EqualTo('password_confirm',message='Both passwords have to match')])
    password_confirm = StringField('Reenter Your Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):

        '''
        function checks if an account in the database already has the provided email
        '''
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('The email already exists')
    def validate_username(self,data_field):

        '''
        function checks if there is already a user with the provided username
        '''
        if User.query.filter_by(username=data_field.data):
            raise ValidationError('The username already exists')

class LoginForm(FlaskForm):

    '''
    class facilitates the creation of login from object
    '''
    email = StringField('Enter Your Email',validators=[Required(),Email()])
    password = StringField('Enter Your Password',validators=[Required()])
    remember = BooleanField("Remember Me")
    submit = StringField('Sign In')