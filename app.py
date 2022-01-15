import os
import datetime
from flask import Flask, render_template
from models.jobs import get_all_jobs
from controllers.jobs_controller import jobs_controller
from controllers.users_controller import users_controller

DB_URL = os.environ.get("DATABASE_URL", "dbname=jobapptrack")
SECRET_KEY = os.environ.get("SECRET_KEY", "TEST_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
year = datetime.datetime.now().year


@app.route('/')
def index():
    jobs = get_all_jobs()
    return render_template("index.html", jobs=jobs, year=year)


app.register_blueprint(jobs_controller)
app.register_blueprint(users_controller)


if __name__ == "__main__":
    app.run(debug=True)
