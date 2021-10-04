from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Any class we make will subclass the declarative base, they will be
# an extension of a main class within the ORM


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")

# Will grab metadata produced by database table schema, creates subclass
# to map everything back to us within the base variable
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"

    # Table schema
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# Create the database using declarative_base subclass
base.metadata.create_all(db)


# Create records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Burners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

john_venkiah = Programmer(
    first_name="John",
    last_name="Venkiah",
    gender="M",
    nationality="Swedish",
    famous_for="World Class Websites"
)


# Add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(john_venkiah)

# Updating a single record
# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous_for = "World President"

# Commit our session to the database
# session.commit()

# Updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# Test to change id to correct after deleting record
people = session.query(Programmer)
newid = 1
for person in people:
    person.id = newid
    newid += 1
newid = 0
session.commit()


# Deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname
# ).first()
# # defensive programming
# if programmer is not None:
#     fullname = programmer.first_name + " " + programmer.last_name
#     print("Programmer Found: ", fullname)
#     confirmation = input("Delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer " + fullname + " has been deleted")
#     else:
#         print("Programmer has not been deleted")
# else:
#     print("No records found")


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

# Query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
