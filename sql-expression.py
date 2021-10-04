from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")  # /// db is locally hosted
meta = MetaData(db)  # data and data about data about tables

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
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Album" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("albumTable.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# make the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(
    #     [artist_table.c.Name])

    # Query 3 - select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Query 4 - select only by "ArtistId" #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select the albums with "ArtistId" #51 from the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select tracks with the composer "Queen" from the "Track" table
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
