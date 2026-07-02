from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic

import ytmusicapi

which_date= input("Which year do you want to travel to ? \n type the date in this formate YYYY-MM-DD :")

url = f"https://appbrewery.github.io/bakeboard-hot-100/{which_date}/"
response = requests.get(url)
print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
songs=[]
ranks=[]
songname = soup.find_all(class_="chart-entry__info")
songrank = soup.find_all(class_="chart-entry__rank")
for song in songname:
    name = song.find(name="h3", class_="chart-entry__title")
    songs.append(name.getText())
print(songs)
for rank in songrank:
    number= rank.find(name="span",class_="chart-entry__rank-number")
    ranks.append(number.getText())

print(ranks)
yt = YTMusic("browser.json")

# playlists = yt.get_library_playlists()
# playlistId = yt.create_playlist(title=f"{which_date}",description="Billboard 100")
# print(f"Found {len(playlists)} playlists in your library.")

# print(playlists)
# print(playlistId)
PLAYLIST_NAME = f"{which_date} Billboard 100"

# Check if playlist already exists
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {which_date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")
for song in songs:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
