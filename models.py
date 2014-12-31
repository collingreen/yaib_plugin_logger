from sqlalchemy import Table, Column, String, DateTime, Text
from modules.persistence import Base, CustomBase


class Log(Base, CustomBase):
    log_type = Column(String(50))
    user = Column(String(200))
    nick = Column(String(100))
    log_time = Column(DateTime)
    channel = Column(String(50))
    message = Column(Text)


class Activity(Base, CustomBase):
    activity_type = Column(String(50))
    user = Column(String(200))
    nick = Column(String(100))
    activity_time = Column(DateTime)
    channel = Column(String(50))
    info1 = Column(String(200))
    info2 = Column(String(200))
