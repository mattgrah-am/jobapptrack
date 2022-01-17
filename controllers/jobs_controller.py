from flask import Blueprint, render_template, request, redirect, session, url_for
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


@jobs_controller.route('/edit', methods=["POST"])
def edit():
    job_data = get_job(request.form.get("id"))
    return redirect(url_for("index", job_data=job_data, show="show"))


@jobs_controller.route('/update', methods=["POST"])
def update():
    update_job(request.form.get("company"),
               request.form.get("role"),
               request.form.get("pay"),
               request.form.get("link"),
               request.form.get("app_date"),
               request.form.get("contact_name"),
               request.form.get("contact_details"),
               request.form.get("app_response"),
               request.form.get("interview_stage"),
               request.form.get("interview_details"),
               request.form.get("offer"),
               request.form.get("job_id"))
    return redirect(url_for("index"))


# @food_controller.route('/delete_food/', methods=["POST"])
# def delete_foods():
#     delete_food(request.form.get("id"))
#     return redirect('/')
