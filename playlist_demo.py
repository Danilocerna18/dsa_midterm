from ll import Node, LinkedList
import time
from memory_profiler import profile


@profile
def create_playlist() -> LinkedList:
    playlist = LinkedList()

    start_time = time.time()

    base_songs = [
        {"name": "Medallo", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Quien TV", "artist": "Blessd", "album": "Hecho en Medellín"},
    ]

    for song in base_songs:
        playlist.insert_at_end(Node(song))

    end_time = time.time()
    print(f"\nTiempo de carga: {end_time:.6f} segundos")

    return playlist
