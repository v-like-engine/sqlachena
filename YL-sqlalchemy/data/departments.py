from sqlalchemy import orm, Column, Integer, String
from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    chief = Column(Integer, nullable=True)
    members = Column(String, nullable=True)
    email = Column(String, nullable=True)

    user = orm.relation('User')
