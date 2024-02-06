#!/usr/bin/env python3
"""Instantiate the Babel object"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Set Babel’s default locale"""
    LANGUAGES = ['en', 'fn']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """The base route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
