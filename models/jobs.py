# IMPORT MODULES
from utilities.database import sql_write, sql_select


def insert_job(user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer):
    # INSERT JOB INTO DB
    sql_write('INSERT INTO jobs(user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', [
              user_id, company, role, float(pay), link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer])


def get_job(id):
    # SELECT JOB FROM DB
    results = sql_select("SELECT * FROM jobs WHERE id = %s", [id])
    if len(results) > 0:
        return results[0]


def get_all_jobs(user_id):
    # SELECT ALL JOBS FROM DB
    results = sql_select('SELECT * FROM jobs WHERE user_id = %s', [user_id])
    if len(results) > 0:
        return results


def update_job(company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer, job_id):
    # UPDATE JOB FROM DB
    sql_write('UPDATE jobs SET company = %s, role = %s, pay = %s, link = %s, app_date = %s, contact_name = %s, contact_details = %s, app_response = %s, interview_stage = %s, interview_details = %s, offer = %s WHERE id = %s;', [
        company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer, job_id])
    print("success")


def delete_job(job_id):
    # DELETE JOB FROM DB
    sql_write('DELETE FROM jobs WHERE id = %s;', [job_id])
