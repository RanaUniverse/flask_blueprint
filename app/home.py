from flask import Blueprint, render_template


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home_page_fun():
    return render_template("home.html")
