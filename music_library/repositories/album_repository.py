from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

#CREATE
def save(album):
    sql = "INSERT INTO albums (album_name, year, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.year, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

#READ/UPDATE
def select(id):

    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_name'], artist, result['year'])

    return album

    
#DELETE
def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)




def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)