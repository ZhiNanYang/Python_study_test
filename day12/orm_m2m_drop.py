#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 13:03:14
# @Author  : Your Name (you@example.org)

import orm_m2m_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m_fk.engine)
s = Session_class()

# author_obj = s.query(orm_m2m_fk.Author).filter(orm_m2m_fk.Author.name == "Jack").first()

# book_obj = s.query(orm_m2m_fk.Book).filter(orm_m2m_fk.Book.name == "跟Alex学把妹").first()

# book_obj.authors.remove(author_obj)

author_obj = s.query(orm_m2m_fk.Author).filter(orm_m2m_fk.Author.name == "Alex").first()
# print(author_obj.name , author_obj.books)
s.delete(author_obj)


s.commit()
