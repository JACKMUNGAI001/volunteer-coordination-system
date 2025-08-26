from models import Base, engine

def main():
    print("Welcome to the Volunteer Coordination System!")
    Base.metadata.create_all(bind=engine)
    print("Database tables created!")

if __name__ == "__main__":
    main()
