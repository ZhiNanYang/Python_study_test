#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 18:35:16
# @Author  : Your Name (you@example.org)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 18:10:17
# @Author  : Your Name (you@example.org)

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

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.name, self.password)

# Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
Session = Session_class()

my_user = Session.query(User).filter_by(id=2).first()
# print(my_user.id, my_user.name, my_user.password)
my_user.name = "alex"

Session.commit()
