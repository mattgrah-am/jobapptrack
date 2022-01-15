from database import sql_write, sql_select
from password import hashpassword


def insert_user(first_name, last_name, email, password, admin):
    ''' INSERT USER INTO DB '''
    password = hashpassword(password)
    sql_write('INSERT INTO users(first_name, last_name, email, password, admin) VALUES (%s, %s, %s, %s, %s);', [
        first_name, last_name, email, password, admin])


def get_user(email):
    ''' SELECT USER INTO DB '''
    row = sql_select("SELECT * FROM users WHERE email = %s", [email])
    return row


def get_all_users():
    ''' SELECT ALL USERS INTO DB '''
    results = sql_select('SELECT * FROM users', [])
    return results


def update_user(first_name, last_name, email, password, user_id):
    ''' UPDATE USER INTO DB '''
    sql_write('UPDATE users SET first_name = %s, last_name = %s, email = %s, SET password = %s, WHERE id = %s;', [
        first_name, last_name, email, password, user_id])


def delete_user(user_id):
    ''' DELETE USER INTO DB '''
    sql_write('DELETE FROM users WHERE id = %s;', [user_id])
