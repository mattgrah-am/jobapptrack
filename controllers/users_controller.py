from flask import Blueprint, render_template, request, redirect, session, url_for
import datetime
from models.users import insert_user, get_user, get_all_users, update_user, delete_user
from password import checkpassword

users_controller = Blueprint("users_controller", __name__)
year = datetime.datetime.now().year


@users_controller.route('/login', methods=["POST"])
def login():
    user = get_user(request.form.get("email"))
    if len(user) > 0 and checkpassword(request.form.get("password"), user[0][4]):
        session['user_id'] = user[0][0]
        session['name'] = user[0][1]
        return redirect(url_for("index"))
    else:
        session['msg'] = "error"
        return redirect(url_for("index"))


@users_controller.route('/logout/')
def logout():
    session.clear()
    return redirect("/")


@users_controller.route('/signup', methods=["POST"])
def signup_user():
    if len(request.form.get("password")) > 3 and request.form.get("password") == request.form.get("confirm_password"):
        insert_user(request.form.get("first_name"),
                    request.form.get("last_name"),
                    request.form.get("email"),
                    request.form.get("password"),
                    "false")
        session['msg'] = "success"
        return redirect('/')
    else:
        session['msg'] = "password_match"
        return redirect('/')


# @users_controller.route('/users/')
# def user_list():
#     users = get_all_users()
#     return render_template("users.html", users=users)
