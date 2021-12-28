import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from os import environ


chosen_date = input("Which year do you want to travel to? Type in following format YYYY-MM-DD: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{chosen_date}/"
SPOTIFY_CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")

response = requests.get(url=BILLBOARD_URL)
webpage = response.text

soup = bs4.BeautifulSoup(webpage, "html.parser")

all_song_names = [song.text.strip() for song in soup.select(selector="li ul li h3")]
all_song_artists = [artist.text.strip() for artist in soup.select(selector="li ul li span")][::7]
print(all_song_names)
print(all_song_artists)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               client_id=SPOTIFY_CLIENT_ID,
                                               redirect_uri="http://example.com",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
song_uris = []
year = chosen_date.split("-")[0]

for song in all_song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 songs of {chosen_date}.", public=False)["id"]
sp.playlist_add_items(playlist_id=playlist, items=song_uris)
