from flask import Blueprint, render_template, request, redirect, session, url_for
import datetime
from models.users import insert_user, get_user, get_users_email, get_all_users, update_user, delete_user
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
        return render_template("index.html", error=True)


@ users_controller.route('/logout/')
def logout():
    session.clear()
    return redirect("/")


@ users_controller.route('/signup', methods=["POST"])
def signup_user():
    emails = get_users_email()
    for i in emails[0]:
        print(i)
        if i == request.form.get("email"):
            return render_template("index.html", email_match_error=True)
    else:
        insert_user(request.form.get("first_name"),
                    request.form.get("last_name"),
                    request.form.get("email"),
                    request.form.get("password"),
                    "false")
        session['signup'] = "success"
        return redirect('/')


# @users_controller.route('/users/')
# def user_list():
#     users = get_all_users()
#     return render_template("users.html", users=users)