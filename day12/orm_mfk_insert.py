#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-05 13:26:18
# @Author  : Your Name (you@example.org)

import orm_mfk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_mfk.engine)
session = Session_class()

# add1 = orm_mfk.Address(street="zhongshanlu", city="QZ", state='FJ')
# add2 = orm_mfk.Address(street="wudaokou", city="Haidian", state='BJ')
# add3 = orm_mfk.Address(street="wuyilu", city="FZ", state='FJ')


# session.add_all([add1, add2, add3])

# s1 = orm_mfk.Customer(name="Rain", billing_address=add1,
#                       shipping_address=add2)
# s2 = orm_mfk.Customer(name="Rain", billing_address=add3,
#                       shipping_address=add3)

# session.add_all([s1, s2])

# session.commit()

obj = session.query(orm_mfk.Customer).filter(
    orm_mfk.Customer.name == "Rain").first()
print(obj.name, obj.billing_address, obj.shipping_address)
