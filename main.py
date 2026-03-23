from ll import Node
from playlist_demo import create_playlist
import random


def play_song(node: Node) -> None:
    data = node.data

    print("\nReproduciendo:")
    print(f"Canción: {data['name']}")
    print(f"Artista: {data['artist']}")
    print(f"Álbum: {data['album']}")


def run() -> None:
    playlist = create_playlist()
    current = playlist.start

    if current is None:
        return

    shuffle_mode = False


    play_song(current)

    while True:
        print("\nOpciones:")
        print("1. Siguiente")
        print("2. Anterior")
        print("3. Shuffle ON/OFF")
        print("4. Salir")

        option = input("Seleccione una opción: ")


        if option == "1":
            if shuffle_mode:
                nodes = [node for node in playlist]
                current = random.choice(nodes)
                play_song(current)

            else:
                if current.next is not None:
                    current = current.next
                    play_song(current)
                else:
                    print("\nLlegaste al final de la lista")


        elif option == "2":
            if shuffle_mode:
                nodes = [node for node in playlist]
                current = random.choice(nodes)
                play_song(current)

            else:
                if current.prev is not None:
                    current = current.prev
                    play_song(current)
                else:
                    print("\nNo hay nada anterior")


        elif option == "3":
            shuffle_mode = not shuffle_mode

            if shuffle_mode:
                print("\nShuffle ACTIVADO")
            else:
                print("\nShuffle DESACTIVADO")


        elif option == "4":
            print("\nSaliendo...")
            break

        else:
            print("\nOpción inválida")


if __name__ == "__main__":
    run()