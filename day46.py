import requests
from bs4 import BeautifulSoup

date = input('Which year would you like to travel to? Type the date in this format YYY-MM-DD: ')
my_url = f'https://www.billboard.com/charts/hot-100/{date}/'
response = requests.get(my_url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
songs = soup.select(selector='li ul li h3')
songs_list = [song.getText().strip() for song in songs]
print(songs_list)

CLIENT_ID = 'fab4ac309861481588aed1a744d7c0e5'
CLIENT_SECRET = 'a0fe4ca6beb54e578f864c8b4fd4a2c6'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Sanjala',
    )
)
user_id = sp.current_user()["id"]

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

uris = []

playlist = sp.user_playlist_create(user=user_id, name=f'{date}BillboardToSpotify', public=False, collaborative=False,
                                   description='Billboard to Spotifyyy')

for song in songs_list:
    # sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))
    result = sp.search(q=f'track:{song}', type='track')
    # pprint.pprint(result)
    try:
        uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'Song {song} doesn not exist')

print(uris)
sp.playlist_add_items(playlist_id=playlist['id'], items=uris)
