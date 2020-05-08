from flask_mail import Message
from flask import render_template
from . import mail

sender_pref = 'Welcome To '
sender_email = 'watchlist.flask@gmail.com'

def welcome_message(subject,template,to,**kwargs):

    '''
    function facilitate the creation of the welcome email that users will receive once they sign up
    '''
    email = Message(subject_pref+subject,sender=sender_email,recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)