from models import SessionLocal, Volunteer, Event, VolunteerEvent

def create_volunteer(name, email):
    session = SessionLocal()
    volunteer = Volunteer(name=name, email=email)
    session.add(volunteer)
    session.commit()
    session.refresh(volunteer)
    session.close()
    return volunteer
