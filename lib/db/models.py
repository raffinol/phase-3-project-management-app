from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(150))
    start_date = Column(DateTime)
    due_date = Column(DateTime)
    urgency = Column(String(10))

class Engineers(Base):
    __tablename__ = 'engineer'

    id = Column(Integer, primary_key=True)




    