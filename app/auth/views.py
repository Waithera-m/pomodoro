from . import auth
from flask import render_template,url_for,redirect,flash,abort,request
from .forms import SignUpForm,LoginForm
from ..models import User
from .. import db
from flask_login import login_user

@auth.route('/login')
def signin():

    '''
    function renders signin template and its contents
    '''
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user=User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid email or password')

    title="Login"

    return render_template('auth/signin.html',login_form=login_form,title=title)

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