from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy as sq

engine = create_engine('postgresql://postgres:1937@localhost:5432/postgres')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = sq.Column(Integer, primary_key=True)
    state = sq.Column(String, default='default')

    search_age_from = sq.Column(Integer, default=16)
    search_age_to = sq.Column(Integer, default=40)

    search_sex = sq.Column(Integer, default=0)
    # search_city = Column(Integer, default=95)
    search_city = sq.Column(Integer)
    search_status = sq.Column(Integer, default=6)

    current_page = sq.Column(String)
    user_views = relationship('Views', back_populates='user')

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<User('%s')>" % self.user_id


class Views(Base):
    __tablename__ = 'views'

    id = sq.Column(Integer, primary_key=True)

    user_id = sq.Column(Integer, ForeignKey('users.user_id'))
    view_id = sq.Column(Integer)

    user = relationship(User, back_populates='user_views')

    def __init__(self, user_id, view_id):
        self.user_id = user_id
        self.view_id = view_id

    def get(self):
        return self.view_id


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
