#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 17:58:00
# @Author  : Your Name (you@example.org)

from sqlalchemy import create_engine, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://yzn:yznyzn@localhost/oldboydb",
                       encoding='utf-8')
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, )
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name: %s>" % (self.id, self.name)


class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("student.id"))

    student = relationship("Student", backref='my_study_record')

    def __repr__(self):
        return "<%s  day: %s, status: %s >\n" % (self.student.name,
                                                 self.day, self.status)


Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()


# s1 = Student(name="Alex", register_date="2014-02-11")
# s2 = Student(name="Jack", register_date="2014-03-11")
# s3 = Student(name="Rain", register_date="2015-02-21")
# s4 = Student(name="Eric", register_date="2014-12-31")

# study_obj1 = StudyRecord(day=1, status="YES", stu_id=1)
# study_obj2 = StudyRecord(day=2, status="NO", stu_id=1)
# study_obj3 = StudyRecord(day=3, status="YES", stu_id=1)
# study_obj4 = StudyRecord(day=1, status="YES", stu_id=2)

# session.add_all([s1, s2, s3, s4, study_obj1,
#                  study_obj2, study_obj3, study_obj4])

# session.commit()


stu_obj = session.query(Student).filter(Student.name == 'Rain').first()
print(stu_obj.my_study_record)
