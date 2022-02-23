# Simple version:
def make_album(artist, title):
    """Return a dictionary containing two pieces of information."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    return album_dict


album = make_album('maroon 5', 'overexposed')
print(album)

album = make_album('the script', 'science and faith')
print(album)

album = make_album('silent sanctuary', 'fuschiang pag-ibig')
print(album)
