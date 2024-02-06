#!/usr/bin/env python3
"""Instantiate the Babel object"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Set Babel’s default locale"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    locale = request.args.get("locale")
    supported_locales = app.config['LANGUAGES']
    if locale in supported_locales:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """The base route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
