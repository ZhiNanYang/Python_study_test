#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 12:35:30
# @Author  : Your Name (you@example.org)

import orm_m2m_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m_fk.engine)
s = Session_class()

# b1 = orm_m2m_fk.Book(name="跟Alex学Python")
# b2 = orm_m2m_fk.Book(name="跟Alex学把妹")
# b3 = orm_m2m_fk.Book(name="跟Alex学装逼")
# b4 = orm_m2m_fk.Book(name="跟Alex学开车")

# a1 = orm_m2m_fk.Author(name="Alex")
# a2 = orm_m2m_fk.Author(name="Jack")
# a3 = orm_m2m_fk.Author(name="Rain")

# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]

# s.add_all([b1, b2, b3, b4, a1, a2, a3])

# s.commit()

print('--------通过书表查关联的作者---------')

book_obj = s.query(orm_m2m_fk.Book).filter(orm_m2m_fk.Book.name == "跟Alex学Python").first()
print(book_obj.name, book_obj.authors)

print('--------通过作者表查关联的书---------')
author_obj = s.query(orm_m2m_fk.Author).filter(orm_m2m_fk.Author.name == "Alex").first()
print(author_obj.name, author_obj.books)
