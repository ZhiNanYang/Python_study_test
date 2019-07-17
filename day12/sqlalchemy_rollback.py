#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 08:21:11
# @Author  : Your Name (you@example.org)

from sqlalchemy_create_table import Session, User


my_user = Session.query(User).filter_by(id=1).first()
my_user.name = "Jack"

fake_user = User(name='Rain', password='123456')
Session.add(fake_user)

print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())

Session.rollback()

print("  &  ", Session.query(User).filter(
    User.name.in_(['Jack', 'rain'])).all())
