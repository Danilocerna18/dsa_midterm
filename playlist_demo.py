

from ll import Node, LinkedList
import time
from memory_profiler import profile


def get_songs():
    return [
        {"name": "Medallo", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Quien TV", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Tendencia Global", "artist": "Blessd", "album": "Si Sabe"},
        {"name": "Instagram", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "AP", "artist": "Blessd", "album": "Single"},
        {"name": "Jordan", "artist": "Ryan Castro", "album": "Single"},
        {"name": "Monastery", "artist": "Ryan Castro", "album": "Single"},
        {"name": "Mujeriego", "artist": "Ryan Castro", "album": "Single"},
        {"name": "Quema", "artist": "Ryan Castro", "album": "Single"},
        {"name": "Wasa Wasa", "artist": "Ryan Castro", "album": "Single"},
        {"name": "Una Noche en Medellín", "artist": "Cris Mj", "album": "Single"},
        {"name": "Marisola", "artist": "Cris Mj", "album": "Single"},
        {"name": "Gata Only", "artist": "Cris Mj", "album": "Single"},
        {"name": "Diabla", "artist": "Cris Mj", "album": "Single"},
        {"name": "Partyson", "artist": "Cris Mj", "album": "Single"},
        {"name": "Normal", "artist": "Feid", "album": "Feliz Cumpleaños Ferxxo"},
        {"name": "Hey Mor", "artist": "Feid", "album": "Feliz Cumpleaños Ferxxo"},
        {"name": "Feliz Cumpleaños Ferxxo", "artist": "Feid", "album": "Feliz Cumpleaños Ferxxo"},
        {"name": "Classy 101", "artist": "Feid", "album": "Single"},
        {"name": "Chorrito Pa Las Animas", "artist": "Feid", "album": "Single"},
        {"name": "Provenza", "artist": "Karol G", "album": "Mañana Será Bonito"},
        {"name": "TQG", "artist": "Karol G", "album": "Mañana Será Bonito"},
        {"name": "Bichota", "artist": "Karol G", "album": "KG0516"},
        {"name": "Amargura", "artist": "Karol G", "album": "Mañana Será Bonito"},
        {"name": "200 Copas", "artist": "Karol G", "album": "KG0516"},
        {"name": "La Inocente", "artist": "Mora", "album": "Microdosis"},
        {"name": "512", "artist": "Mora", "album": "Primer Día de Clases"},
        {"name": "Memorias", "artist": "Mora", "album": "Microdosis"},
        {"name": "Volando", "artist": "Mora", "album": "Microdosis"},
        {"name": "Calentón", "artist": "Mora", "album": "Microdosis"},
        {"name": "Dakiti", "artist": "Bad Bunny", "album": "El Último Tour del Mundo"},
        {"name": "Tití Me Preguntó", "artist": "Bad Bunny", "album": "Un Verano Sin Ti"},
        {"name": "Moscow Mule", "artist": "Bad Bunny", "album": "Un Verano Sin Ti"},
        {"name": "Callaita", "artist": "Bad Bunny", "album": "Single"},
        {"name": "Yonaguni", "artist": "Bad Bunny", "album": "Single"},
        {"name": "Pepas", "artist": "Farruko", "album": "La 167"},
        {"name": "La Tóxica", "artist": "Farruko", "album": "La 167"},
        {"name": "Krippy Kush", "artist": "Farruko", "album": "TrapXficante"},
        {"name": "Besas Tan Bien", "artist": "Farruko", "album": "Single"},
        {"name": "Obsesionado", "artist": "Farruko", "album": "Visionary"},
        {"name": "China", "artist": "Anuel AA", "album": "Single"},
        {"name": "Secreto", "artist": "Anuel AA", "album": "Single"},
        {"name": "Ella Quiere Beber", "artist": "Anuel AA", "album": "Real Hasta la Muerte"},
        {"name": "Adicto", "artist": "Anuel AA", "album": "Single"},
        {"name": "Keii", "artist": "Anuel AA", "album": "Las Leyendas Nunca Mueren"},
        {"name": "Relación", "artist": "Sech", "album": "1 of 1"},
        {"name": "Otro Trago", "artist": "Sech", "album": "Sueños"},
        {"name": "911", "artist": "Sech", "album": "42"},
        {"name": "Sal y Perrea", "artist": "Sech", "album": "1 of 1"},
        {"name": "Ignorantes", "artist": "Sech", "album": "Single"},
        {"name": "Bandido", "artist": "Myke Towers", "album": "Single"},
        {"name": "La Playa", "artist": "Myke Towers", "album": "Easy Money Baby"},
        {"name": "Diosa", "artist": "Myke Towers", "album": "Easy Money Baby"},
        {"name": "Experimento", "artist": "Myke Towers", "album": "Single"},
        {"name": "Lala", "artist": "Myke Towers", "album": "Single"},
        {"name": "Sensual Bebé", "artist": "Jhayco", "album": "Timelezz"},
        {"name": "Dakiti Remix", "artist": "Jhayco", "album": "Single"},
        {"name": "No Me Conoce", "artist": "Jhayco", "album": "Famouz"},
        {"name": "En Mi Cuarto", "artist": "Jhayco", "album": "Timelezz"},
        {"name": "Ley Seca", "artist": "Jhayco", "album": "Single"},
        {"name": "Lokera", "artist": "Rauw Alejandro", "album": "Single"},
        {"name": "Todo de Ti", "artist": "Rauw Alejandro", "album": "Vice Versa"},
        {"name": "Desesperados", "artist": "Rauw Alejandro", "album": "Vice Versa"},
        {"name": "Punto 40", "artist": "Rauw Alejandro", "album": "Single"},
        {"name": "Tattoo", "artist": "Rauw Alejandro", "album": "Afrodisíaco"},
        {"name": "X Última Vez", "artist": "Daddy Yankee", "album": "Legendaddy"},
        {"name": "Gasolina", "artist": "Daddy Yankee", "album": "Barrio Fino"},
        {"name": "Con Calma", "artist": "Daddy Yankee", "album": "Single"},
        {"name": "Dura", "artist": "Daddy Yankee", "album": "Single"},
        {"name": "Limbo", "artist": "Daddy Yankee", "album": "Prestige"},
        {"name": "Mi Gente", "artist": "J Balvin", "album": "Single"},
        {"name": "Ginza", "artist": "J Balvin", "album": "Energía"},
        {"name": "Ay Vamos", "artist": "J Balvin", "album": "La Familia"},
        {"name": "Rojo", "artist": "J Balvin", "album": "Colores"},
        {"name": "Azul", "artist": "J Balvin", "album": "Colores"},
        {"name": "Ella Baila Sola", "artist": "Peso Pluma", "album": "Single"},
        {"name": "PRC", "artist": "Peso Pluma", "album": "Single"},
        {"name": "AMG", "artist": "Peso Pluma", "album": "Single"},
        {"name": "Lady Gaga", "artist": "Peso Pluma", "album": "Single"},
        {"name": "Rubicon", "artist": "Peso Pluma", "album": "Génesis"},
        {"name": "BZRP #52", "artist": "Bizarrap", "album": "Single"},
        {"name": "BZRP #53", "artist": "Bizarrap", "album": "Single"},
        {"name": "BZRP #54", "artist": "Bizarrap", "album": "Single"},
        {"name": "BZRP #55", "artist": "Bizarrap", "album": "Single"},
        {"name": "BZRP #56", "artist": "Bizarrap", "album": "Single"},
        {"name": "Luna", "artist": "Feid", "album": "Ferxxocalipsis"},
        {"name": "Ferxxo 100", "artist": "Feid", "album": "Ferxxocalipsis"},
        {"name": "Ey Chory", "artist": "Feid", "album": "Ferxxocalipsis"},
        {"name": "Yandel 150", "artist": "Yandel", "album": "Single"},
        {"name": "Encantadora", "artist": "Yandel", "album": "Dangerous"},
        {"name": "Nunca Me Olvides", "artist": "Yandel", "album": "Dangerous"},
        {"name": "Moviendo Caderas", "artist": "Yandel", "album": "De Líder a Leyenda"},
        {"name": "Te Suelto el Pelo", "artist": "Yandel", "album": "Single"},
        {"name": "La Jeepeta", "artist": "Nio Garcia", "album": "Single"},
        {"name": "AM Remix", "artist": "Nio Garcia", "album": "Single"},
        {"name": "Travesuras", "artist": "Nio Garcia", "album": "Single"},
        {"name": "Infiel", "artist": "Nio Garcia", "album": "Single"},
        {"name": "Te Boté", "artist": "Nio Garcia", "album": "Single"}
    ]


@profile
def create_playlist() -> LinkedList:
    playlist = LinkedList()


    start_time = time.time()

    base_songs = get_songs()

    for song in base_songs:
        playlist.insert_at_end(Node(song))


    end_time = time.time()


    total_time = end_time - start_time

    print(f"\nTiempo de carga (end - start): {end_time:.6f} - {start_time:.6f} = {total_time:.6f} segundos")

    return playlist