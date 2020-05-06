from . import auth
from flask import render_template,url_for,redirect,flash,abort

@auth.route('/login')
def sign_in():

    '''
    function renders signin template and its contents
    '''
    return render_template('auth/signin.html')