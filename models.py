from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///volunteers.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Volunteer(Base):
    __tablename__ = "volunteers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    volunteers = relationship("VolunteerEvent", back_populates="event")

class VolunteerEvent(Base):
    __tablename__ = "volunteer_events"

    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, ForeignKey("volunteers.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

    volunteer = relationship("Volunteer", back_populates="events")
    event = relationship("Event", back_populates="volunteers")

Volunteer.events = relationship("VolunteerEvent", back_populates="volunteer")
