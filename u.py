database = input()
global_init(database)

db_sess = create_session()

for user in db_sess.query(User).filter(User.address == 'module_1', 'engineer' NOT IN User.speciality, 'engineer' NOT IN User.position).all():
    print(user.id)