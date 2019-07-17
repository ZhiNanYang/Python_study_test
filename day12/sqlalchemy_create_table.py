#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 14:25:43
# @Author  : Your Name (you@example.org)

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://yzn:yznyzn@localhost/oldboydb",
                       encoding='utf-8')
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr(self):
        return "<User(name=%s, password=%s)>" % (self.name, self.password)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()
