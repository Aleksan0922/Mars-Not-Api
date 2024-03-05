database = input()
global_init(database)

db_sess = create_session()

for job in db_sess.query(Jobs.filter(Jobs.work_size < 20, Jobs.is_finished == 0)).all():
    print(f'{job} {job.job}')