from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")  # /// db is locally hosted

# create "Artist" table variable
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String)
    Column("ArtistId", Integer, primary_key=True),
)

meta = MetaData(db)  # data and data about data about tables

# make the connection
with db.connect() as connection:
