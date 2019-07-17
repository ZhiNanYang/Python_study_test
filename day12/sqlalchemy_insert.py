#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 17:53:17
# @Author  : Your Name (you@example.org)

import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://yzn:yznyzn@localhost/oldboydb",
                       encoding="utf-8")
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
Session = Session_class()

user_obj1 = User(name="Jack", password="123456")
user_obj2 = User(name="Rain", password="589658")
user_obj3 = User(name="Chen", password="874599")
user_obj4 = User(name="Tomas", password="123456")

# print(user_obj.name, user_obj.id)

Session.add_all([user_obj1, user_obj2, user_obj3, user_obj4])
# print(user_obj.name, user_obj.id)

Session.commit()
