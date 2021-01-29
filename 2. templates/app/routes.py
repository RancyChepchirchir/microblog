from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rancy'}
    posts = [
        {
            'author': {'username': 'Rancy'},
            'body': 'Beautiful day in Sweden!'
        },
        {
            'author': {'username': 'Hannah'},
            'body': 'The Big Bang Theory movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
