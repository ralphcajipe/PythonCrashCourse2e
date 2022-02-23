# With tracks version:
def make_album(artist, title, tracks=0):
    """Return a dictionary containing two pieces of information."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


album = make_album('maroon 5', 'overexposed')
print(album)

album = make_album('the script', 'science and faith')
print(album)

album = make_album('silent sanctuary', 'fuschiang pag-ibig')
print(album)

album = make_album('one direction', 'midnight memories', tracks=14)
print(album)
