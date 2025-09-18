from datetime import datetime

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from .app import profile_bp

fake_user = {"email": "rana@rana.com", "password": "123"}


@profile_bp.get("/")
def profile_home():
    return render_template("index.html")


@profile_bp.get("/login")
def show_login_fun():
    return render_template("login.html")


@profile_bp.post("/login")
def process_login_fun():
    email = request.form.get("email")
    password = request.form.get("password")

    if email == fake_user["email"] and password == fake_user["password"]:
        return redirect(url_for("profile.dashboard_fun"))

    else:
        flash("Invalid Email / Password, Please Check Again", "error")
        return redirect(url_for("profile.show_login_fun"))


@profile_bp.get("/dashboard")
def dashboard_fun():
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template(
        "dashboard.html",
        login_time=login_time,
    )
