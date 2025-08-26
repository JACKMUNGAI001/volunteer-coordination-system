import click
from crud import create_volunteer, create_event, list_volunteers, list_events, assign_volunteer_to_event
from models import Base, engine
from tabulate import tabulate

@click.group()
def cli():
    """Volunteer Coordination System CLI"""
    pass

@cli.command()
def initdb():
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized successfully!")

@cli.command()
@click.argument("name")
@click.argument("email")
def add_volunteer(name, email):
    volunteer = create_volunteer(name, email)
    click.echo(f"Volunteer {volunteer.name} added with email {volunteer.email}.")

@cli.command()
@click.argument("title")
@click.argument("description")
def add_event(title, description):
    event = create_event(title, description)
    click.echo(f"Event {event.title} added.")

@cli.command()
@click.argument("volunteer_id", type=int)
@click.argument("event_id", type=int)
def assign(volunteer_id, event_id):
    assign_volunteer_to_event(volunteer_id, event_id)
    click.echo(f"Volunteer {volunteer_id} assigned to event {event_id}.")

@cli.command()
def volunteers():
    data = list_volunteers()
    table = [(v.id, v.name, v.email) for v in data]
    click.echo(tabulate(table, headers=["ID", "Name", "Email"]))

@cli.command()
def events():
    data = list_events()
    table = [(e.id, e.title, e.description) for e in data]
    click.echo(tabulate(table, headers=["ID", "Title", "Description"]))


if __name__ == "__main__":
    cli()
