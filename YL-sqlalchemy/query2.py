global_init(input())
db = create_session()

for user in db.query(User).filter(User.address == 'module_1',
                                  User.position.notlike('%ingeneer%'),
                                  User.speciality.notlike('%ingeneer%')):
    print(user.id)
