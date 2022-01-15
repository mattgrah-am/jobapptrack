from flask import Blueprint, render_template, request, redirect, session
import datetime
from models.jobs import insert_job, get_job, get_all_jobs, update_job, delete_job


jobs_controller = Blueprint("jobs_controller", __name__)
year = datetime.datetime.now().year


# @food_controller.route('/create/')
# def create():
#     if session.get('user_id'):
#         return render_template('create.html', year=year)
#     else:
#         return redirect("/")


# @food_controller.route('/food', methods=["POST"])
# def insert():
#     insert_food(request.form.get("name"),
#                 request.form.get("price"),
#                 request.form.get("image_url"),
#                 request.form.get("description"))
#     return redirect('/')


# @food_controller.route('/update/')
# def update():
#     if session.get('user_id'):
#         results = get_all_food()
#         return render_template('update.html', year=year, results=results)
#     else:
#         return redirect("/")


# @food_controller.route('/edit/<id>/', methods=["GET"])
# def edit(id):
#     if session.get('user_id'):
#         row = get_food(id)
#         return render_template('edit.html', food_item=row)
#     else:
#         return redirect("/")


# @food_controller.route('/update_food/', methods=["POST"])
# def update_foods():
#     update_food(request.form.get("name"),
#                 request.form.get("price"),
#                 request.form.get("image_url"),
#                 request.form.get("description"),
#                 request.form.get("id"))
#     return redirect('/')


# @food_controller.route('/delete_food/', methods=["POST"])
# def delete_foods():
#     delete_food(request.form.get("id"))
#     return redirect('/')
