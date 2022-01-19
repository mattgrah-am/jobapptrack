from database import sql_write, sql_select


def insert_job(user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer):
    '''INSERT JOB INTO DB'''
    sql_write('INSERT INTO jobs(user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', [
              user_id, company, role, float(pay), link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer])


def get_job(id):
    '''SELECT JOB FROM DB'''
    rows = sql_select("SELECT * FROM jobs WHERE id = %s", [id])
    row = rows[0]
    return row


def get_all_jobs():
    '''SELECT ALL JOBS FROM DB'''
    results = sql_select('SELECT * FROM jobs', [])
    jobs = []
    for item in results:
        jobs.append(
            [item[0], item[1],  item[2],  item[3], f'${(item[4]):.2f}', item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12]])
    return jobs


def update_job(company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer, job_id):
    '''UPDATE JOB FROM DB'''
    sql_write('UPDATE jobs SET company = %s, role = %s, pay = %s, link = %s, app_date = %s, contact_name = %s, contact_details = %s, app_response = %s, interview_stage = %s, interview_details = %s, offer = %s WHERE id = %s;', [
        company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer, job_id])
    print("success")


def delete_job(job_id):
    '''DELETE JOB FROM DB'''
    sql_write('DELETE FROM jobs WHERE id = %s;', [job_id])
