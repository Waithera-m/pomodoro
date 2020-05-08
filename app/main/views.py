from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import EditProfile
from .. import db,photos
from flask_login import login_required
import tkinter as Tkinter

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

    counter=-1
    running = False
    def counter_label(label):
        def count():
            if running:
                global counter

                if counter==-1:
                    display="Starting..."
                
                label['text']=display

                label.after(1000,count)
                counter += 1
        count()

    def start(label):

        '''
        function starts stopwatch
        '''
        global running
        running=True
        counter_label(label)
        start['state']='disabled'
        stop['state']='normal'
        reset['state']='normal'
    
    def stop(label):

        '''
        function stops stopwatch
        '''
        global running
        start['state']='normal'
        stop['state']='disabled'
        reset['state']='normal'
        running=False
    
    def reset(label):

        '''
        function resets stopwatch
        '''
        global counter
        counter=-1

        if running==False:
            reset['state']='disabled'
            label['text']='Set Your Time'
        else:
            label['text']='Starting'

    root = Tkinter.Tk()
    root.title('Stopwatch')

    root.minsize(width=250, height=70) 
    label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
    label.pack() 
    start = Tkinter.Button(root, text='Start',  
    width=15, command=lambda:Start(label)) 
    stop = Tkinter.Button(root, text='Stop',  
    width=15, state='disabled', command=Stop) 
    reset = Tkinter.Button(root, text='Reset', 
    width=15, state='disabled', command=lambda:Reset(label)) 
    start.pack() 
    stop.pack() 
    reset.pack() 
    root.mainloop() 
    
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



