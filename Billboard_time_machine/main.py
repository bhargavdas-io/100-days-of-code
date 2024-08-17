import os
from bs4 import BeautifulSoup
import requests
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_PLAYLIST_ENDPOINT = "https://api.spotify.com/v1/users/{user_id}/playlists"
BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'
CID = os.environ["SPOTIPY_CLIENT_ID"]
CIS = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
USERNAME = os.environ["USER_ID"]

#---------OAuth----------#

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CID,
        client_secret=CIS,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,

    )
)

user_id = sp.current_user()["id"]
date = input("Where do you want to go back in time? Type the date in YYYY-MM-DD format: ")
url = requests.get(url=BILLBOARD_URL + date)
data = url.text
soup = BeautifulSoup(data, 'html.parser')
test = soup.select("li ul li h3")
top_100s = [song.getText().strip() for song in test]

song_uris = []
year = date.split("-")[0]
for song in top_100s:
    result = sp.search(q=f"track: {song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")

pprint(song_uris)

playlist = sp.user_playlist_create(
    user=USERNAME,
    name=f"{date} Billboard Hot 100",
    public=False,

)

playlist_id = playlist['id']

add_tracks = sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris,

)
