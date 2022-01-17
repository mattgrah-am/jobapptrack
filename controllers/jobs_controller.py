from flask import Blueprint, render_template, request, redirect, session
import datetime
from models.jobs import insert_job, get_job, get_all_jobs, update_job, delete_job


jobs_controller = Blueprint("jobs_controller", __name__)
year = datetime.datetime.now().year


@jobs_controller.route('/newjob', methods=["POST"])
def add_job():
    user = session["user_id"]
    insert_job(user,
               request.form.get("company"),
               request.form.get("role"),
               request.form.get("pay"),
               request.form.get("link"),
               request.form.get("app_date"),
               request.form.get("contact_name"),
               request.form.get("contact_details"),
               request.form.get("app_response"),
               request.form.get("interview_stage"),
               request.form.get("interview_details"),
               request.form.get("offer"))
    return redirect('/')


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
