from models import Project, Engineers
from random import choice as random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projects-data.db")
Session = sessionmaker(bind=engine)
session = Session()

from faker import Faker

fake = Faker()

session.query(Engineers).delete()
session.query(Project).delete()

levels = ["junior", "mid", "senior"]
for _ in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    engineer = Engineers(name=first_name, last_name=last_name, level=random(levels))
    print(engineer)

urgency = ["high", "medium", "low"]
for _ in range(10):
    title = fake.text(max_nb_chars=50)
    description = fake.text(max_nb_chars=150)
    start_date = fake.past_date()
    due_date = fake.future_date()
    project = Project(
        title=title,
        description=description,
        start_date=start_date,
        due_date=due_date,
        urgency=random(urgency),
    )
    print(project)

import ipdb

ipdb.set_trace()
