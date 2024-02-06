#!/usr/bin/env python3
"""Instantiate the Babel object"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import UnknownTimeZoneError
import datetime


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
    """Function that returns a user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Use get_user to find a user if any, and set it as a global"""
    g.user = get_user()
    # if g.user:
    #     locale = g.user['locale'] or app.config['BABEL_DEFAULT_LOCALE']
    #     babel.locale_selector_func = lambda: locale


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    locale = request.args.get("locale")
    if locale:
        return locale if locale in app.config['LANGUAGES'] else None
    if g.user and 'locale' in g.user:
        return g.user['locale'] if g.user['locale'] in\
            app.config['LANGUAGES'] else None
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the best match for the timezone."""
    user = getattr(g, 'user', None)
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if user and 'timezone' in user:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    return 'UTC'

@app.route('/')
def index():
    """The base route"""
    timezone = get_timezone()
    current_time = datetime.datetime.now(pytz.timezone(timezone)).strftime('%H:%M:%S')
    return render_template('index.html', user=g.user, current_time=current_time)


if __name__ == '__main__':
    app.run()
