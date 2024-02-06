#!/usr/bin/env python3
"""Instantiate the Babel object"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Set Babel’s default locale"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Function that returns a user dictionary or None"""
    user = request.args.get('login_as')
    if user:
        return users.get(int(user))
    return None


@app.before_request
def before_request():
    """ use get_user to find a user if any, and set it as a global"""
    user = get_user()
    g.user = user


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
