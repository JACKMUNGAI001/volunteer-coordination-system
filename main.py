import click
from crud import create_volunteer, create_event, list_volunteers, list_events, assign_volunteer_to_event
from models import Base, engine

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo("Welcome to the Volunteer Coordination System!")
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized!")

@cli.command()
@click.argument("name")
@click.argument("email")
def add_volunteer(name, email):
    volunteer = create_volunteer(name, email)
    click.echo(f"Volunteer {volunteer.name} added.")

@cli.command()
@click.argument("title")
@click.argument("description")
def add_event(title, description):
    event = create_event(title, description)
    click.echo(f"Event {event.title} added.")
   
   

if __name__ == "__main__":
    cli()
