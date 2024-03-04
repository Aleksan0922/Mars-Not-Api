from flask import Flask
from flask import render_template, request, redirect
from data.jobs import Jobs
from data import db_session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")


def main():
    app.run(host='127.0.0.1', port=5000)


@app.route('/')
def promotion_image():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    return render_template('index.html', jobs=db_sess.query(Jobs).all(), i=0)


if __name__ == '__main__':
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False

    job1 = Jobs()
    job1.team_leader = 2
    job1.job = 'deployment of residential modules 3 and 2'
    job1.work_size = 18
    job1.collaborators = '1, 3'
    job1.start_date = datetime.datetime.now()
    job1.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    main()