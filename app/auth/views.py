from . import auth
from flask import render_template,url_for,redirect,flash,abort
from .forms import SignUpForm
from ..models import User
from .. import db

@auth.route('/login')
def signin():

    '''
    function renders signin template and its contents
    '''
    return render_template('auth/signin.html')

@auth.route('/register',methods=["GET","POST"])
def register():
    
    '''
    view function renders registration template and its contents
    '''
    form = SignUpForm()

    if form.validate_on_submit():

        user = User(username=form.username.data,email=form.email.data,password=form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.signin'))

        title = 'New Account'

    return render_template('auth/register.html',form=form,title=title)