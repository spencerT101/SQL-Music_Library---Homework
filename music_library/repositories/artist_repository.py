from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

   

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
   sql = "DELETE FROM artists WHERE id = %s"
   values = [id]
   run_sql(sql, values)

def albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql)

    


