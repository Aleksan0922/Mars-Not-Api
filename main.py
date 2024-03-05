from flask import Flask
from flask import render_template, request, redirect
from wtforms.fields.simple import StringField

from data.jobs import Jobs
from data import db_session
import datetime
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask import Flask
from flask import render_template, request, redirect
from flask_login import LoginManager, login_user
from data.users import User
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init("db/mars_explorer.db")


def main():
    app.run(host='127.0.0.1', port=5000)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddJobForm(FlaskForm):
    team_leader = IntegerField('Id капитана', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Продолжительность работы', validators=[DataRequired()])
    collaborators = StringField('Id работников', validators=[DataRequired()])
    start_date = DateTimeField('Начало работ', default=datetime.datetime.now())
    end_date = DateTimeField('Конец работ')
    is_finished = BooleanField('Закончено ли дело')
    submit = SubmitField('Добавить')

@app.route('/')
def index():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    return render_template('index.html', jobs=db_sess.query(Jobs).all(), i=0)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
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
        return render_template('index.html')
    return render_template('forms.html', title='Добавить работу', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


if __name__ == '__main__':
    main()