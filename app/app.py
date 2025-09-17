from flask import Flask

from .home import home_bp
from .notes import notes_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(notes_bp,url_prefix="/notes")

    return app
