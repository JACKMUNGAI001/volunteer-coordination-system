import click
from crud import create_volunteer, create_event, list_volunteers, list_events, assign_volunteer_to_event
from models import Base, engine

def cli():
    pass

def initdb():
    click.echo("Welcome to the Volunteer Coordination System!")
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized!")

if __name__ == "__main__":
    cli()
