
from data import db_session
from data.user import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
db = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"

user1 = User()
user1.surname = "Scott 1"
user1.name = "Ridley"
user1.age = 21
user1.position = "colonist"
user1.speciality = "research engineer"
user1.address = "module_1"
user1.email = "scott1_bad_colonist@mars.org"

user2 = User()
user2.surname = "Scott 2"
user2.name = "Ridley"
user2.age = 21
user2.position = "colonist"
user2.speciality = "research engineer"
user2.address = "module_1"
user2.email = "scott2_mega_colonist@mars.org"

user3 = User()
user3.surname = "Scott 3"
user3.name = "Ridley"
user3.age = 21
user3.position = "colonist"
user3.speciality = "research engineer"
user3.address = "module_1"
user3.email = "scott3_super_colonist@mars.org"

db.add(user)
db.add(user1)
db.add(user2)
db.add(user3)

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False

db.add(job)

job = Jobs()
job.team_leader = 1
job.job = 'asdasdasdasd'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False

db.add(job)

job = Jobs()
job.team_leader = 1
job.job = 'asdasdasd'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = True

db.add(job)

db.commit()