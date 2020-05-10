global_init(input())
db = create_session()
    
for user in db.query(User).filter(User.address == 'module_1'):
    print(user)

