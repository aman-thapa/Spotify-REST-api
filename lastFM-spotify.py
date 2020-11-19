import json
import requests
import secrets

class lastFMsoptify:
    def __init__(self):
        self.token = secrets.spotify_token()
        self.api_key = secrets.last_fm_api_key()
        self.user_id = secrets.spotify_user_id()
        self.headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        self.playlist_id = ''

    def fetch_songs_from_lastfm(self):
        pass

    def get_uri_from_spotify(self):
        pass

    def create_spotify_playlist(self):
        pass

    def add_songs_to_playlist(self):
        pass

    def list_songs_in_playlist(self):
        pass
