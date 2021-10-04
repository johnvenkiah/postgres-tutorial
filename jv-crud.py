from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Piano(base):
    __tablename__ = "Piano"

    # Table schema
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    nr_of_keys = Column(Integer)
    genres = Column(String)


# Ask for a session, create new inst of sessionmaker, pointng to engine (db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# Create the database using declarative_base subclass
base.metadata.create_all(db)


# Create records on our Programmer table
rhodes = Piano(
    name="Fender Rhodes",
    type="Electric",
    nr_of_keys=73,
    genres=("Soul", "Funk", "Jazz")
)


upright = Piano(
    name="Acoustic Upright",
    type="Acoustic",
    nr_of_keys=88,
    genres=("Jazz", "Soul")
)


clavinet = Piano(
    name="Hohner D6",
    type="Electric",
    nr_of_keys=76,
    genres=("Funk", "Soul", "Reggae")
)


organ = Piano(
    name="Hammond B3",
    type="Electric",
    nr_of_keys=122,
    genres=("Jazz", "Funk", "Soul", "Reggae")
)

# session.add(rhodes)
# session.add(upright)
# session.add(clavinet)
# session.add(organ)
# session.commit()


# Updating a single record
# piano = session.query(Piano).filter_by(id=4).first()
# piano.genres = "Soul"

# # Commit our session to the database
# session.commit()

# Updating multiple records
# instrs = session.query(Piano)
# for pi in instrs:
#     if (",") in pi.genres:
#         pi.genres = "Jazz"
#     session.commit()

# Deleting a single record
pi = input("Enter a piano to delete: ")
piano = session.query(Piano).filter_by(
    name=pi).first()
# defensive programming
if piano is not None:
    confirmation = input(f"Delete {piano.name}? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(piano)
        session.commit()
        print(piano.name + " has been deleted")
    else:
        print("Piano has not been deleted")
else:
    print(f"{pi} Not found")

# Deleting a single record


# Query the database to find all pianos
pianos = session.query(Piano)
for piano in pianos:
    print(
        piano.id,
        piano.name,
        piano.type,
        piano.nr_of_keys,
        piano.genres,
        sep=" | "
    )





# Deleting multiple records - ONLY USE IF SURE TO DELETE ALL!
# programmers = session.query(Programmer)
# delete_confmtion = input("Delete all (irreversible)? (y/n) ")

# if delete_confmtion == "y":
#     for programmer in programmers:
#         session.delete(programmer)
#         session.commit()
#         print("All records deleted")
# else:
#     print("No records deleted")
