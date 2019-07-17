#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 13:13:45
# @Author  : Your Name (you@example.org)

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='yznyzn', db='oldboy')
cursor = conn.cursor()

cursor.execute("select * from student;")
print(cursor.fetchmany(3))
conn.commit()
cursor.close()
conn.close()
