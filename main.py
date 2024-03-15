from flask import make_response, jsonify
from data.jobs import Jobs
from data import db_session, jobs_api
import datetime
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired
from wtforms.fields.simple import StringField

from flask import Flask, abort
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import reqparse, abort, Api, Resource
from data.users import User
from data.users_resource import UsersResource, UsersListResource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init("db/mars_explorer.db")


def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(host='127.0.0.1', port=5000)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class JobForm(FlaskForm):
    team_leader = IntegerField('Id капитана', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Продолжительность работы', validators=[DataRequired()])
    collaborators = StringField('Id работников', validators=[DataRequired()])
    start_date = DateTimeField('Начало работ', default=datetime.datetime.now())
    end_date = DateTimeField('Конец работ')
    is_finished = BooleanField('Закончено ли дело')
    submit = SubmitField('Добавить')


class DepartmentForm(FlaskForm):
    chief = IntegerField('Id капитана', validators=[DataRequired()])
    title = StringField('Описание отдела', validators=[DataRequired()])
    members = StringField('Id сотрудников', validators=[DataRequired()])
    email = EmailField('Почта отдела', validators=[DataRequired()])
    submit = SubmitField('Добавить')


@app.route('/')
def index():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    return render_template('index.html', jobs=db_sess.query(Jobs).all(), i=0)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        job = Jobs()
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.start_date = form.start_date.data
        job.end_date = form.end_date.data
        job.is_finished = form.is_finished.data

        db_sess = db_session.create_session()
        db_sess.add(job)
        db_sess.commit()
        return redirect('index.html')
    return render_template('forms.html', title='Добавить работу', form=form)


@app.route('/job_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id, current_user.id == 1 |
                                          current_user.id == Jobs.team_leader).first()
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.start_date.data = jobs.start_date
            form.end_date.data = jobs.end_date
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id, current_user.id == 1 |
                                          current_user.id == Jobs.team_leader).first()
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.start_date = form.start_date.data
            jobs.end_date = form.end_date.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('forms.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departments')
def departments():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    return render_template('departments.html', jobs=db_sess.query(Jobs).all(), i=0)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"Jobs {jobs_id} not found")


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    # для списка объектов
    api.add_resource(UsersListResource, '/api/v2/users')

    # для одного объекта
    api.add_resource(UsersResource, '/api/v2/user/<int:user_id>')
    main()