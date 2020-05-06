from . import main
from flask import render_template

@main.route('/')
def index():

    '''
    view function renders index template and its contents
    '''
    title='Pomodoro'
    return render_template('index.html',title=title)