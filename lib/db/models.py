from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(150))
    start_date = Column(DateTime)
    due_date = Column(DateTime)
    urgency = Column(String(10))

    engineer_id = Column(Integer, ForeignKey("engineer.id"))

    def __repr__(self):
        return (
            f"\n<project "
            + f"id={self.id}, "
            + f"title={self.title}, "
            + f"description={self.description}, "
            + f"start_date={self.start_date}, "
            + f"due_date={self.due_date}, "
            + f"urgency={self.urgency}, "
            + " >"
        )


class Engineers(Base):
    __tablename__ = "engineer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    level = Column(String(10))

    projects = relationship("Project", backref="engineer")

    def __repr__(self):
        return (
            f"\n<engineer "
            + f"id={self.id}, "
            + f"name={self.name}, "
            + f"last_name={self.last_name}, "
            + f"level={self.level}, "
            + " >"
        )
