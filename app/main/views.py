from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User

@main.route('/')
def index():

    '''
    view function renders index template and its contents
    '''
    title='Pomodoro'
    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):

    '''
    function returns profile page and its contents
    '''
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html",user=user)