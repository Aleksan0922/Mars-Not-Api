from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.db")


def main():
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "yamete_kudasai"
    user.modified_date = datetime.datetime.now()

    user1 = User()
    user1.surname = "yqgyuqug"
    user1.name = "sdfdsgsf"
    user1.age = 14
    user1.position = "qwerttt"
    user1.speciality = "Пользоgghrhfnfватель"
    user1.address = "porhorjbmepv"
    user1.email = "email@email.ru"
    user1.hashed_password = "howefhocnjncoe"
    user1.modified_date = datetime.datetime.now()

    user2 = User()
    user2.surname = "dfjonef"
    user2.name = "wevervev"
    user2.age = 9999999
    user2.position = "tyntyhtynt"
    user2.speciality = "rtberbetb"
    user2.address = "porhoynydyfddesftbyrrjbmepv"
    user2.email = "email@email.com"
    user2.hashed_password = "dead_inside"
    user2.modified_date = datetime.datetime.now()

    user3 = User()
    user3.surname = "hdttymrtmu"
    user3.name = "dymr5udrmu"
    user3.age = 1
    user3.position = "effibevore"
    user3.speciality = "eoknvorbnob"
    user3.address = "kjdoepjve"
    user3.email = "email@emil.ru"
    user3.hashed_password = "nagibator228"
    user3.modified_date = datetime.datetime.now()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()