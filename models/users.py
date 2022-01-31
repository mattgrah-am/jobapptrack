# IMPORT MODULES
from utilities.database import sql_write, sql_select
from utilities.password import hashpassword


def insert_user(first_name, last_name, email, password, admin):
    # INSERT USER INTO DB
    password = hashpassword(password)
    sql_write('INSERT INTO users(first_name, last_name, email, password, admin) VALUES (%s, %s, %s, %s, %s);', [
        first_name, last_name, email, password, admin])


def get_user(email):
    # SELECT USER INTO DB
    results = sql_select("SELECT * FROM users WHERE email = %s", [email])
    if len(results) > 0:
        return results[0]
    return None


def get_users_email():
    # SELECT USER INTO DB
    emails = sql_select("SELECT email FROM users", [])
    return emails


def update_user(first_name, last_name, email, password, user_id):
    # UPDATE USER INTO DB
    sql_write('UPDATE users SET first_name = %s, last_name = %s, email = %s, SET password = %s, WHERE id = %s;', [
        first_name, last_name, email, password, user_id])


def delete_user(user_id):
    # DELETE USER INTO DB
    sql_write('DELETE FROM users WHERE id = %s;', [user_id])
