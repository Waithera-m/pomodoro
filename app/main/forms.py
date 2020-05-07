from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from ..models import User
from wtforms.validators import Required

class EditProfile(FlaskForm):

    '''
    class facilitates the creation of edit profile form objects
    '''
    bio = TextAreaField('Let the world know you', validators=[Required()])
    submit= SubmitField('Add Bio')
