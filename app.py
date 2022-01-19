import os
import datetime
from flask import Flask, render_template, session
from models.jobs import get_all_jobs
from controllers.jobs_controller import jobs_controller
from controllers.users_controller import users_controller

SECRET_KEY = os.environ.get("SECRET_KEY", "TEST_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
year = datetime.datetime.now().year


@app.route('/')
def index():
    jobs = get_all_jobs()
    if type(session.get('job_data')) is not tuple:
        session['job_data'] = None
        session['show'] = ""
        return render_template("index.html", jobs=jobs, year=year)
    else:
        return render_template("index.html", jobs=jobs, year=year, show=session['show'])


app.register_blueprint(jobs_controller)
app.register_blueprint(users_controller)


if __name__ == "__main__":
    app.run(debug=True)
