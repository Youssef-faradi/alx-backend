#!/usr/bin/env python3
"""Tsk 3: Basic Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Config class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Renders an HTML page
    with a title and a header.
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
