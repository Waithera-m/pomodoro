from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import EditProfile
from .. import db,photos
from flask_login import login_required
import time

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

@main.route('/user/<uname>/edit', methods=["GET","POST"])
def edit_profile(uname):

    '''
    view function returns edit profile template and its contents
    '''
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    
    edit_form = EditProfile()

    if edit_form.validate_on_submit():
        user.bio = edit_form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))
    
    return render_template('profile/edit.html',edit_form=edit_form)

@main.route('/user/<uname>/edit/pic',methods=["POST"])
@login_required
def update_pic(uname):

    '''
    view function process file upload submission request
    '''

    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_photo_path=path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



