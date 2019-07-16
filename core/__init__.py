import os
from flask import Flask, render_template, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def welcome():
        naem='Rishu'
        return render_template('welcome.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    return app

