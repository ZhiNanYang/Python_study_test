from sqlalchemy import Column, Integer, String, create_engine,func
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
session = Session_class()

# my_user = Session.query(User).filter(User.id == 1).first()
# my_user = Session.query(User).filter(User.id < 7).filter(User.id > 3).all()
# my_user = Session.query(User).filter(User.name.like("ra%")).count()
my_user = session.query(func.count(User.name), User.name).group_by(
    User.name).all()

# print(my_user.id, my_user.name, my_user.password)
print(my_user)
