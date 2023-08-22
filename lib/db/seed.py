from models import Project, Engineers
from random import choice as random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projects-data.db")
Session = sessionmaker(bind=engine)
session = Session()

from faker import Faker

fake = Faker()

levels = ["junior", "mid", "senior"]
for _ in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    engineer = Engineers(name=first_name, last_name=last_name, level=random(levels))
    print(engineer)


import ipdb

ipdb.set_trace()
