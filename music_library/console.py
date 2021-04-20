import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

album_1 = Album("Revolutionary, Vol.1", "2001")
album_repository.save(album_1)

album_2 = Album("Grand Champ", "2003")
album_repository.save(album_2)

album_3 = Album("It's Dark And Hell Is Hot", "1998")
album_repository.save(album_3)

artist_1 = Artist("Immortal Technique")
artist_repository.save(artist_1)

artist_2 = Artist("DMX")
artist_repository.save(artist_2)




pdb.set_trace()
