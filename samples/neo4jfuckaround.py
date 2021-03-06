from time import time

import pandas as pd
from neomodel import config

from model.graph.spotify.track import Track


def main():
    # TODO: change password
    s = time()
    config.DATABASE_URL = "bolt://neo4j:PyRate69@localhost:7687"
    song: Track = Track.nodes.first_or_none(uri='spotify:track:2okfdBLRlJaCR4uMJdvqsY')
    print('Acousticness', song.acousticness)
    print('Danceability', song.danceability)
    print('Energy', song.energy)
    print('Instrumentalness', song.instrumentalness)
    print('Key', song.key)
    print('Liveness', song.liveness)
    print('Mode', song.mode)
    print('Popularity', song.popularity)
    print('Speechiness', song.speechiness)
    print('Tempo', song.tempo)
    print('Time Signature', song.time_signature)
    print(song)
    print(s - time(), 'seconds')

    data = {}
    for playlist in song.playlists:
        for track in playlist.tracks:
            cols = [track.acousticness, track.danceability, track.energy, track.instrumentalness, track.key,
                    track.liveness, track.mode, track.popularity,
                    track.speechiness, track.tempo, track.time_signature]
            data[track.spotify_id] = cols

    data = [[key, *val] for key, val in data.items()]
    df = pd.DataFrame(data, columns=['ID', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key',
                                     'liveness', 'mode', 'popularity', 'speechiness', 'tempo', 'time_signature'])
    print(df)