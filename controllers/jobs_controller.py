# IMPORT MODULES
from flask import Blueprint, request, redirect, session, url_for
from models.jobs import insert_job, get_job, update_job, delete_job


jobs_controller = Blueprint("jobs_controller", __name__)


@jobs_controller.route('/jobs/newjob', methods=["POST"])
def add_job():
    # TAKE FORM DATA AS A JOB AND INSERT INTO JOB DATABASE
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
    session['job_data'] = None
    session['show'] = ""
    return redirect(url_for("index"))


@jobs_controller.route('/jobs/<id>/edit')
def edit(id):
    # GET JOB DATA FROM DATABASE AND RETURN AS LIST AND ASSIGN TO SESSION
    session['job_data'] = get_job(id)
    session['show'] = "show"
    return redirect(url_for("index"))


@jobs_controller.route('/jobs/<id>/update', methods=["POST"])
def update(id):
    # TAKE FORM DATA AND UDATE JOB DATA FROM DATABASE
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
               id)
    session['job_data'] = None
    session['show'] = ""
    return redirect(url_for("index"))


@jobs_controller.route('/jobs/<id>/delete')
def deletejob(id):
    delete_job(id)
    session['job_data'] = None
    session['show'] = ""
    return redirect(url_for("index"))
