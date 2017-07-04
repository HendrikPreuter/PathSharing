from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(id='%s', username='%s', password='%s', email='%s')>" % (
            self.id, self.username, self.password, self.email)


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    admin = Column(String)
    name = Column(String)

    def __repr__(self):
        return "<User(id='%s', description='%s', admin='%s', name='%s')>" % (
            self.id, self.description, self.admin, self.name)
