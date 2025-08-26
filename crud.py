from models import SessionLocal, Volunteer, Event, VolunteerEvent

def create_volunteer(name, email):
    session = SessionLocal()
    volunteer = Volunteer(name=name, email=email)
    session.add(volunteer)
    session.commit()
    session.refresh(volunteer)
    session.close()
    return volunteer

def create_event(title, description):
    session = SessionLocal()
    event = Event(title=title, description=description)
    session.add(event)
    session.commit()
    session.refresh(event)
    session.close()
    return event
