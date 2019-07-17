#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 08:49:04
# @Author  : Your Name (you@example.org)

from sqlalchemy_create_table import Session, User

print(Session.query(User.name, User.id).all())
